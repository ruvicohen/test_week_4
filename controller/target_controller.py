from dataclasses import asdict

from flask import Blueprint, jsonify

from dto.response_dto import ResponseDto
from repository.target_repository import find_target_by_id, find_targets
from utils.general_utils import to_dict

target_blueprint = Blueprint("user", __name__)


@target_blueprint.route("/", methods=["GET"])
def get_targets():
    targets = find_targets()
    targets_dict = [to_dict(target) for target in targets]
    response = ResponseDto(body={"targets": targets_dict})
    return jsonify(asdict(response)), 200

@target_blueprint.route("/<int:t_id>", methods=['GET'])
def get_target(t_id: int):
    return (
        find_target_by_id(t_id)
        .map(to_dict)
        .map(lambda t: (jsonify(asdict(ResponseDto(body={"target": t}))), 200))
        .value_or((jsonify(asdict(ResponseDto(body={}))), 404))
    )


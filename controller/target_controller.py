from dataclasses import asdict
from flask import Blueprint, jsonify
from returns.maybe import Maybe
from dto.response_dto import ResponseDto
from repository.target_repository import find_target_by_id, find_targets
from utils.general_utils import to_dict

target_blueprint = Blueprint("user", __name__)

@target_blueprint.route("/", methods=["GET"])
def get_targets():
    return(
        Maybe.from_optional(find_targets()).
        map(lambda targets: list(map(to_dict, targets))).
        map(lambda t: (jsonify(asdict(ResponseDto(body={"targets": t}))), 200))
        .value_or((jsonify(asdict(ResponseDto(body={}))), 404))

    )
@target_blueprint.route("/<int:t_id>", methods=['GET'])
def get_target(t_id: int):
    return (
        find_target_by_id(t_id)
        .map(to_dict)
        .map(lambda t: (jsonify(asdict(ResponseDto(body={"target": t}))), 200))
        .value_or((jsonify(asdict(ResponseDto(body={}))), 404))
    )


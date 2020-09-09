from dataclasses import asdict
from flask import Blueprint, jsonify, request
from returns.maybe import Maybe, Nothing, Some
from toolz.curried import partial

from dto.response_dto import ResponseDto
from repository.target_repository import find_target_by_id, find_targets, update_target, delete_target, insert_target
from service.target_service import convert_to_target
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

@target_blueprint.route("/create", methods=['POST'])
def create_target_c():
    return (
        convert_to_target(request.json)
        .bind(insert_target)
        .map(to_dict)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 400))
    )

@target_blueprint.route("/update/<int:t_id>", methods=['POST'])
def update_target_c(u_id: int):
    return (
        convert_to_target(request.json)
        .bind(lambda x: Some(x) if find_target_by_id(u_id) else Nothing)
        .map(partial(update_target, u_id))
        .map(lambda x: to_dict(x.value_or(None)))
        .map(lambda u: (jsonify(asdict(ResponseDto(body={"user": u}))), 200))
        .value_or((jsonify(asdict(ResponseDto(body={}))), 404))
    )

@target_blueprint.route("/delete/<int:t_id>", methods=['GET'])
def delete_target_c(u_id: int):
    return (
        find_target_by_id(u_id)
        .bind(lambda a: delete_target(a.id))
        .map(to_dict)
        .map(lambda u: (jsonify(asdict(ResponseDto(body={"user": u}))), 200))
        .value_or((jsonify(asdict(ResponseDto(body={}))), 404))
    )
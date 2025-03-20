from flask import Blueprint, jsonify

producs_routes_bp = Blueprint("products_routes", __name__)

@producs_routes_bp.route("/products", methods=["POST"])
def insert_product():
    return jsonify({"msg": "produto cadastrado"}), 200


@producs_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name):
    return jsonify({"msg": f"produto {product_name}"}), 200
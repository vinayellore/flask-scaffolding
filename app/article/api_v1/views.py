from flask import Blueprint, jsonify, request
from models.article import Article
from app.article.serializers import articles_schema, article_schema, article_create_schema, article_update_schema

article_api_blueprint = Blueprint(
    'article_api', __name__,
)


@article_api_blueprint.route("/", methods=['GET', 'POST'], strict_slashes=False)
def articles():
    """view for get articles"""
    if request.method == "GET":
        articles = articles_schema.dump(Article.query.all())
        return jsonify({"success": True, "articles": articles.data}), 200

    article_data = article_create_schema.load(request.get_json() or {})
    if article_data.errors:
        return jsonify({**article_data.errors, "success": False}), 401
    article_data = article_data.data
    article = Article(
        name=article_data.get('name'),
        author=article_data.get('author'),
        description=article_data.get('description', '')
    )
    article.save()
    article_data["id"] = article.id
    return jsonify({"success": True, "article": article_data}), 201


@article_api_blueprint.route("/<int:id>", methods=['GET'])
def article_details(id):
    article = Article.query.get(id)
    if not article:
        return jsonify({"success": False, "message": "Article not found"}), 404
    article = article_schema.dump(article)
    return jsonify({"success": True, "article": article.data}), 200


# @article_api_blueprint.route("/", methods=['POST'], strict_slashes=False)
# def new_article():
#     article_data = article_create_schema.load(request.get_json() or {})
#     if article_data.errors:
#         return jsonify({**article_data.errors, "success": False}), 401
#     article_data = article_data.data
#     article = Article(
#         name=article_data.get('name'),
#         author=article_data.get('author'),
#         description=article_data.get('description', '')
#     )
#     article.save()
#     article_data['id'] = article.id
#     return jsonify({"success": True, "article": article_data}), 201


@article_api_blueprint.route("/update/<int:id>", methods=['PUT'])
def update_article(id):
    article_serializer = article_update_schema.load(request.get_json() or {})
    if article_serializer.errors:
        return jsonify({**article_serializer.errors, "success": False}), 401
    article_data = article_serializer.data
    article = Article.query.get(id)
    if not article:
        return jsonify({"success": False, "message": "Article not found"}), 404
    article.name = article_data.get('name', article.name)
    article.author = article_data.get('author', article.author)
    article.description = article_data.get('description', article.description)
    article.save()
    return jsonify({"success": True, "article": article_data}), 200


@article_api_blueprint.route("/delete/<int:id>", methods=['DELETE'])
def delete_article(id):
    try:
        Article.query.get(id).delete()
        return jsonify({"success": True, "message": "Article deleted successfully."}), 200
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": "Article not found."}), 404

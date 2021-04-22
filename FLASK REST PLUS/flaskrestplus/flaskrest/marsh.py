from flask import Flask
from flask_restplus import Api, Resource, fields
from marshmallow import Schema, fields as ma_fields,post_load
app = Flask(__name__)
api = Api(app)
class TheLanguage(object):
    def __init__(self, language, framework):
        self.language = language
        self.framework = framework
    def __repr__(self):
        return '{} is the language. {} is the framework'.format(self.language, self.framework)

class LanguageSchema(Schema):
    language = ma_fields.String()
    framework = ma_fields.String()
    @post_load
    def create_language(self, data, **kwargs):
        return TheLanguage(**data)
a_language = api.model('Language',
                       {'language': fields.String('The language.'), 'framework': fields.String('The framework')})
languages = []
# python = {'language': 'Python', 'id': 1}
python = TheLanguage(language='Python', framework='Flask')
languages.append(python)
@api.route('/language')
class Language(Resource):
    # @api.marshal_with(a_language, envelope='the_data')
    def get(self):
        schema = LanguageSchema(many=True)  # list of objets
        return schema.dump(languages)  # converts to JSON object
    @api.expect(a_language)
    def post(self):
        schema = LanguageSchema()
        new_language = schema.load(api.payload)
        print(new_language)
        # new_language['id'] = len(languages) + 1
        # languages.append(new_language)
        return {'result': 'Language added'}, 201
if __name__ == '__main__':
    app.run(debug=True)

















from exts import app
import re


# hash_filter_test.py
# import jinja2
# from hash_filter import j2_hash_filter
#
# env = jinja2.Environment()
#
#
# tmpl = env.from_string(tmpl_string)
# # @app.template_filter('contain_str')
# def contain_str(matchstr, origin_str):
#     return re.search(matchstr, origin_str)

@app.template_test('end_with')
def end_with(matchstr, suffix):
    return matchstr.lower().endswith(suffix.lower())


# app.jinja_env.tests['end_with'] = end_with

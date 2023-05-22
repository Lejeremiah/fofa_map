import lxml.html
import urllib.parse as urlparse

class ContentsHandler():
    def __init__(self):
        pass
    def get_contents_by_cssselect(self,html_string_and_code):
        html_string_broken = html_string_and_code['html']
        html_tree_broken = lxml.html.fromstring(html_string_broken)
        # html_string_pretty = lxml.html.tostring(html_tree_broken,pretty_print=True)
        # html_tree_pretty = lxml.html.tostring(html_string_pretty)
        html_tree_pretty = html_tree_broken

        divs_href_and_content = html_tree_pretty.cssselect('span.hsxa-host')
        for div in divs_href_and_content:
            content = div.text_content()
            content = content.replace('\n','').replace(' ','')
            if 'http' in content:
                result = content
            else:
                result = 'http://' + content
            print(result)



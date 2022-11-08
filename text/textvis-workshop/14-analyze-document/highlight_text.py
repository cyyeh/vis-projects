

# class to highlight select tokens in a set of tokens.
class HighlightText:
    ''' Highlight a subset of tokens in a token list.
    '''
    def __init__(self, tokens, highlights=[], color='red'):
        self.tokens = tokens
        self.highlights = highlights
        self.color = color

    def _repr_html_(self):
        html = ["<p>"]
        for token in self.tokens:
            if token in self.highlights:
                html.append("<span style='color:" + self.color + "'>" + token + " </span>")
            else:
                html.append(token + ' ')
        html.append("</p>")
        return ''.join(html)

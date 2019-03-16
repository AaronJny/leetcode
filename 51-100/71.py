class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        i = 0
        n = len(path)
        paths = [x for x in path.split('/') if x]
        for x in paths:
            if x == '.':
                continue
            if x == '..':
                if len(result):
                    result.pop()
                continue
            result.append(x)
        if len(result):
            return '/{}'.format('/'.join(result))
        else:
            return '/'
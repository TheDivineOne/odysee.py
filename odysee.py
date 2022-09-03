import requests,ast

def getVideoMetadata(url,timeout=7):
     return ast.literal_eval(requests.get(url,timeout=timeout).text.split('<script type="application/ld+json">')[1].split("</script>")[0])

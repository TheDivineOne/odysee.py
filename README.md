# odysee.py
Usage example:
```python
import odysee
metadata = odysee.getVideoMetadata("https://odysee.com/@DivineSoftware:8/noclip")
print(metadata)
```
```
$ python example.py
{'@context': 'https://schema.org', '@type': 'VideoObject', 'name': 'NoClip - Crypto Clipper/Stealer protection | Simple clipboard monitor', 'description': '[Downloads]\nMEGA: https://mega.nz/file/n8VGnTBQ#2d48yIFzfM2HVAyXulSAIy-GWtHJjxlIcb7bf_m3DQM\nKeyBase: https://keybase.pub/divine_software/mirror/FreeReleases/NoClip.exe', 'thumbnailUrl': 'https://thumbnails.odycdn.com/card/s:1280:720/quality:85/plain/https://thumbs.odycdn.com/edc0624d7ee77fc57fdc02b178ee25ac.webp', 'uploadDate': '2022-09-02T13:30:14.000Z', 'duration': 'PT40S', 'url': 'https://odysee.com/@DivineSoftware:8/noclip:1', 'contentUrl': 'https://player.odycdn.com/api/v3/streams/free/noclip/1239005e4d787148a106848055c58cf84917891a/d47b79.mp4', 'embedUrl': 'https://odysee.com/$/embed/noclip/1239005e4d787148a106848055c58cf84917891a', 'author': {'@type': 'Person', 'name': 'Divine Software', 'url': 'https://odysee.com/@DivineSoftware:8'}, 'thumbnail': {'@type': 'ImageObject', 'url': 'https://thumbnails.odycdn.com/card/s:1280:720/quality:85/plain/https://thumbs.odycdn.com/edc0624d7ee77fc57fdc02b178ee25ac.webp'}, 'keywords': 'antivirus,crypto,stealer,protection,programming', 'width': 1920, 'height': 1034, 'potentialAction': {'@type': 'SeekToAction', 'target': 'https://odysee.com/@DivineSoftware:8/noclip:1?t={seek_to_second_number}', 'startOffset-input': 'required name=seek_to_second_number'}}
```

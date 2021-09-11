# 1、找到未加密的参数
# 2、想办法按照网易的方式加密参数，params->encText，encSecKey->encSecKey
# 3、请求到网易，拿到评论信息
# https://music.163.com/weapi/comment/resource/comments/get?csrf_token=
# post


url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

# 加密的信息
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1825647671",
    "threadId": "R_SO_4_1825647671"
}
# 处理加密过程
d = data
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "dU36xtGMeAq7FNBI"

def getencSecKey() :
    return "701ce40f0ddfcb39779ba96c4a7d08f4121c632f8fde70ff1c9a50fb860bb58594f82408671625ef75fafabd09435a93036fd3427cbef80a9f2069c436507fec32bd9b0b00ee10add9d425cce82ea426715a93c09948dd7874e4b768d10d43af44dc3535797646a5afce691c56033ce2edf7e157a9ecc24a8dcc47a8c143e628"

'''
    function a(a) { 十六个随机数
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { d : data数据 e : 010001 f : 一串 g : 0CoJUm6Qyw8W8jud
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
'''
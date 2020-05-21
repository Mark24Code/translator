
import argparse
import urllib.request
import urllib.parse
import json

# 有道翻译方法


def youdao_translate(content):
    '''实现有道翻译的接口'''
    youdao_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}

    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1525141473246'
    data['sign'] = '47ee728a4465ef98ac06510bf67f3023'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('utf-8')

    youdao_response = urllib.request.urlopen(youdao_url, data)
    youdao_html = youdao_response.read().decode('utf-8')
    target = json.loads(youdao_html)

    trans = target['translateResult']
    ret = ''
    for i in range(len(trans)):
        line = ''
        for j in range(len(trans[i])):
            line = trans[i][j]['tgt']
        ret += line + '\n'

    return ret


def translate(context):
    result = youdao_translate(context)

    print('-----------')
    print('原文: {}'.format(context))
    print('---')
    print('译文: {}'.format(result))
    print('-----------')
    return result


parser = argparse.ArgumentParser(description='python3 translate')
parser.add_argument('--word', '-w', help='translate word')
parser.add_argument('--file', '-f', help='translate file path')

args = parser.parse_args()

if args.word:
    translate(args.word)

elif args.file:
    translate_result = None
    with open(args.file) as f:
        context = f.readlines()
        translate_result = translate("".join(context))

    if translate_result:
        with open('./translated.txt', 'w') as t:
            t.writelines(translate_result)

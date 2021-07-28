from .models import RankingInfo
from django.views.generic import View
from django.http import JsonResponse
import json


class Score(View):

    def post(self, request):
        j_data = json.loads(request.body)
        client = j_data.get('client')
        score = j_data.get('score')
        user = RankingInfo.objects.filter(client=client)
        if user:
            RankingInfo.objects.filter(client=client).update(score=score)
            return JsonResponse({'code': 200, 'data': 'Update Success!'})
        RankingInfo.objects.create(client=client, score=score)
        return JsonResponse({'code': 200, 'data': 'Save Success!'})

    def get(self, request):
        client = request.GET.get('client')
        start = int(request.GET.get('start'))
        limit = int(request.GET.get('limit'))
        rank_info = RankingInfo.objects.order_by('-score')[start:limit]
        data = []
        for info in rank_info:
            row = {}
            row['rank'] = info.id
            row['client'] = info.client
            row['score'] = info.score
            data.append(row)

        self_info = RankingInfo.objects.get(client=client)  # 查看排行客户添加
        data.append({'id': self_info.id, 'client': self_info.client, 'score': self_info.score})

        return JsonResponse({'code': 200, 'data': data})

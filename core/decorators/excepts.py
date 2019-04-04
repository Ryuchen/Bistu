#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 11:24 
# @Author : ryuchen
# @Site :  
# @File : execpts.py 
# @Desc : 
# ==================================================
import logging

from rest_framework import status
from django.http import JsonResponse

from core.exceptions.errors import *

log = logging.getLogger('default')


def excepts(func):
    """
    进行异常捕获的装饰器，通过装饰方法捕获django在处理过程中发生的错误，其中由view层raise出异常，然后通过捕获之后统一返回给前台标准的错误信息
    Example:
        in views.py:
        @excepts
        def functions(request):
            if request.method != "GET":
                raise NotImplementedError
                ~~~
        in excepts.py
        try:
            return func(*args, **kwargs)
        except NotImplementedError:
            ~~~

    采用标准错误回执格式，如下：
    {
         "meta": {
            "message": "Invalid API key.",   // 前台提示用户的错误信息
            "details": "",        // 需要前台帮忙记录的后端错误信息
            "retryable": false    // 相同请求体内容是否允许客户端继续尝试提交
         },
         "data" : {}
    }
    接口状态码则由统一的http状态信息返回
    """
    def handle_except(*args, **kwargs):
        res = {
            "meta": {
                "message": "",
                "details": {},
                "retryable": True,
                "code": ""
            },
            "data": {
            }
        }
        try:
            return func(*args, **kwargs)
        except AuthenticateError as e:
            res["meta"]['message'] = 'Unauthenticated'
            res["meta"]["details"] = "{0}".format(e.details)
            res["meta"]['code'] = e.code
            return JsonResponse(res, status=e.code)
        except ForbiddenError as e:
            res["meta"]['message'] = 'Forbidden'
            res["meta"]["details"] = "{0}".format(e.details)
            res["meta"]['code'] = e.code
            return JsonResponse(res, status=e.code)
        except ConnectionError as e:
            res["meta"]['message'] = 'Engine connection error'
            res["meta"]["details"] = "{0}".format(e)
            res["meta"]['code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            return JsonResponse(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except NotImplementedError as e:
            res["meta"]['message'] = 'METHOD NOT ALLOWED'
            res["meta"]["details"] = "{0}".format(e)
            res["meta"]['code'] = status.HTTP_405_METHOD_NOT_ALLOWED
            return JsonResponse(res, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except MemoryError as e:
            res["meta"]['message'] = 'Method not allowed'
            res["meta"]["details"] = "{0}".format(e)
            res["meta"]['code'] = status.HTTP_405_METHOD_NOT_ALLOWED
            return JsonResponse(res, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except (TypeError, KeyError, SyntaxError, ValueError, AttributeError) as e:
            log.error("{0}".format(e), exc_info=True)
            res["meta"]['message'] = 'BAD REQUEST'
            res["meta"]["details"] = "{0}".format(e)
            res["meta"]['code'] = status.HTTP_400_BAD_REQUEST
            return JsonResponse(res, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            res["meta"]['message'] = 'Server error'
            res["meta"]["details"] = "{0}".format(e)
            res["meta"]['code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            return JsonResponse(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return handle_except


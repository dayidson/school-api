# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from school_api.session import SessionStorage


class RedisStorage(SessionStorage):

    def __init__(self, redis):
        for method_name in ('get', 'set', 'delete'):
            assert hasattr(redis, method_name)
        self.redis = redis

    def key_name(self, key):
        return '{0}:{1}'.format(self.prefix, key)

    def get(self, key, default=None):
        key = self.key_name(key)
        value = self.redis.get(key)
        if value is None:
            return default
        return json.loads(value)

    def set(self, key, value, ttl=None):
        if value is None:
            return
        key = self.key_name(key)
        value = json.dumps(value)
        self.redis.set(key, value, ex=ttl)

    def delete(self, key):
        key = self.key_name(key)
        self.redis.delete(key)

    def __call__(self, prefix='school'):
        self.prefix = prefix
        return self

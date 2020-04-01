"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
Object.defineProperty(exports, "__esModule", { value: true });
var cache_storage_1 = require("../cache-storage");
var url_1 = require("url");
var logger_1 = require("../logger");
exports.proxy = 'http://example.com/proxy';
exports.createMockContext = function (origin, opts) {
    if (opts === void 0) { opts = {}; }
    var context = {
        location: {
            href: origin
        },
        document: {
            createElement: function (_name) {
                var _href = '';
                return {
                    set href(value) {
                        _href = value;
                    },
                    get href() {
                        return _href;
                    },
                    get protocol() {
                        return new url_1.URL(_href).protocol;
                    },
                    get hostname() {
                        return new url_1.URL(_href).hostname;
                    },
                    get port() {
                        return new url_1.URL(_href).port;
                    }
                };
            }
        }
    };
    cache_storage_1.CacheStorage.setContext(context);
    logger_1.Logger.create('test');
    return cache_storage_1.CacheStorage.create('test', __assign({ imageTimeout: 0, useCORS: false, allowTaint: false, proxy: exports.proxy }, opts));
};
//# sourceMappingURL=mock-context.js.map
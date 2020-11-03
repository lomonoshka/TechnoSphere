from collections import defaultdict


def smartdict_nan(key):
    return 10 * key


N = 10

smartdict = {}
for key in range(N):
    val = defaultdict(lambda key=key: smartdict_nan(key))
    smartdict[key] = val

"""
Проблема изначальной реализации заключается в следующем - при обращении к несуществующему ключу, как и должно быть
в defaultdict, вызывалась функция по умолчанию, которую мы задали как lambda: smartdict_nan(key). При ее вызове
переменная key искалась по правилу поиска LEGB: Local -> Enclosed -> Global -> Built-in. И так как после выполнения
цикла, переменная key стала равна 9, то он и использовал это значение. Чтобы это исправить я в нашей функции по
умолчанию конкретно указал чему должна быть равна переменная key. Тем самым она нашлась в локальной области
видимости.
"""

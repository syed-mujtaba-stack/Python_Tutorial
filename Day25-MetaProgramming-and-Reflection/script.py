# Day 25 Script: Metaprogramming & Reflection Demo
class PluginBase:
    pass

def plugin_func(self):
    print('Plugin loaded!')

PluginBase.run = plugin_func
p = PluginBase()
p.run()

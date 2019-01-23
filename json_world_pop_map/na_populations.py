import pygal.maps.world

# 获取世界地图
wm =  pygal.maps.world.World()
# 设置标题
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('svg/na_populations.svg')
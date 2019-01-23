* 代码托管在[这儿](https://github.com/cn-Wziv/alien_invasion)
* 本项目是一个以抵御外星入侵为背景的射击类游戏
* 编程语言：Python
* 主要扩展包：pygame

** 主要模块及方法概述 **
* ```alien_invasion.py``` ：游戏的初始化和各个模块的实例化
	* ```run_game()```：初始化游戏，游戏内主要功能的调用

* ```alien.py``` ：创建和管理外星人
	* ```__init__()``` ：初始化外星人相关各个属性
	* ```check_edges()``` ：判断外星人是否到达左右边界
	* ```update()``` ：外星人的自动移动
	* ```blitme()``` ：在制定位置绘制外星人

* ```bullet.py``` ：管理飞船发射的子弹，继承自pygame.Sprite类
	* ```__init__()``` ：初始化子弹的相关属性
	* ```update()``` ：子弹自动向上移动
	* ```draw_bullet()``` ：在屏幕上绘制子弹

* ```button.py``` ：创建和管理按钮
	* ```__init__()``` ：初始化按钮的相关属性
	* ```prep_msg()``` ：将相关信息渲染为图像，并添加到按钮上
	* ```draw_button()``` ：绘制按钮

* ```game_function()``` ：核心文件，游戏的主要方法
	* ```check_keydown_event()``` ：响应按键下压事件
	* ```check_keyup_event()``` ：响应按键弹起事件
	* ```check_events()``` ：响应按键和鼠标事件
	* ```check_play_button()``` ：响应鼠标点击事件
	* ```fire_button()``` ：发射子弹
	* ```update_screen()``` ：更新屏幕上的图像
	* ```update_bullets()``` ：更新飞行的子弹的图像
	* ```check_high_score()``` ：检测是否产生了新的最高分
	* ```check_bullet_alien_collosion()``` ：响应子弹和外星人碰撞事件
	* ```check_fleet_edges()``` ：检测外星人群是否到达左右边缘
	* ```change_fleet_direction()``` ：改变外星人群的飞行轨迹
	* ```ship_hit()``` ：响应飞船被外星人撞击事件
	* ```check_aliens_bottom)``` ：检测外星人是否到达屏幕底部
	* ```update_aliens()``` ：更新外星人群的移动方向
	* ```get_number_aliens_x()``` ：计算每行可容纳多少外星人
	* ```get_number_rows()``` ：计算可容纳多少行外星人
	* ```create_alien()``` ：创建外星人
	* ```create_fleet()``` ：创建外星人群

* ```game_stats.py``` ：游戏相关统计数据
	* ```__init__()``` ：初始化游戏相关统计信息
	* ```reset_stats()``` ：初始化游戏过程中经常变化的属性，重置游戏属性

* ```scoreboard.py``` ：显示游戏得分
	* ```__init__()```初始化游戏得分相关属性
	* ```prep_score()``` ：显示分数
	* ```prep_high_score()``` ：显示最高分
	* ```prep_level()``` ：显示等级
	* ```prep_ships()``` ：显示剩余飞船数
	* ```show_score()``` ：在屏幕上显示得分、等级、最高分

* ```setting.py``` ：用于存储游戏中用到的各种设置
	* ```__init__()``` ：初始化游戏中的静态设置
	* ```initialize_dynamic_settings()``` ：初始化随游戏进行改变的动态设置
	* ```increase_speed()``` ：提高速度设置

* ```ship.py``` ：飞船属性和方法
	* ```__init__()``` ：飞船相关属性的初始化
	* ```center_ship()``` ：将飞船居中
	* ```update()``` ：根据移动标志调整飞船位置，限制飞船移动范围
	* ```blitme()``` ：在指定位置绘制飞船
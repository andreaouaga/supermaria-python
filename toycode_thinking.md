pygame的游戏逻辑：画图<--->更新　不断循环

pygame.display

pygame module to control the display window and screen
pygame.display.init
Initialize the display module
pygame.display.quit
Uninitialize the display module
pygame.display.get_init
Returns True if the display module has been initialized
pygame.display.set_mode
Initialize a window or screen for display
pygame.display.get_surface
Get a reference to the currently set display surface
pygame.display.flip
Update the full display Surface to the screen
pygame.display.update
Update portions of the screen for software displays
pygame.display.get_driver
Get the name of the pygame display backend
pygame.display.Info
Create a video display information object
pygame.display.get_wm_info
Get information about the current windowing system
pygame.display.list_modes
Get list of available fullscreen modes
pygame.display.mode_ok
Pick the best color depth for a display mode
pygame.display.gl_get_attribute
Get the value for an OpenGL flag for the current display
pygame.display.gl_set_attribute
Request an OpenGL display attribute for the display mode
pygame.display.get_active
Returns True when the display is active on the screen
pygame.display.iconify
Iconify the display surface
pygame.display.toggle_fullscreen
Switch between fullscreen and windowed displays
pygame.display.set_gamma
Change the hardware gamma ramps
pygame.display.set_gamma_ramp
Change the hardware gamma ramps with a custom lookup
pygame.display.set_icon
Change the system image for the display window
pygame.display.set_caption
Set the current window caption
pygame.display.get_caption
Get the current window caption
pygame.display.set_palette
Set the display color palette for indexed displays
pygame.display.get_num_displays
Return the number of displays
pygame.display.get_window_size
Return the size of the window or screen
This module offers control over the pygame display. Pygame has a single display Surface that is either contained in a window or runs full screen. Once you create the display you treat it as a regular Surface. Changes are not immediately visible onscreen; you must choose one of the two flipping functions to update the actual display.

The origin of the display, where x = 0 and y = 0, is the top left of the screen. Both axes increase positively towards the bottom right of the screen.

The pygame display can actually be initialized in one of several modes. By default, the display is a basic software driven framebuffer. You can request special modules like hardware acceleration and OpenGL support. These are controlled by flags passed to pygame.display.set_mode().

Pygame can only have a single display active at any time. Creating a new one with pygame.display.set_mode() will close the previous display. If precise control is needed over the pixel format or display resolutions, use the functions pygame.display.mode_ok(), pygame.display.list_modes(), and pygame.display.Info() to query information about the display.

Once the display Surface is created, the functions from this module affect the single existing display. The Surface becomes invalid if the module is uninitialized. If a new display mode is set, the existing Surface will automatically switch to operate on the new display.

When the display mode is set, several events are placed on the pygame event queue. pygame.QUIT is sent when the user has requested the program to shut down. The window will receive pygame.ACTIVEEVENT events as the display gains and loses input focus. If the display is set with the pygame.RESIZABLE flag, pygame.VIDEORESIZE events will be sent when the user adjusts the window dimensions. Hardware displays that draw direct to the screen will get pygame.VIDEOEXPOSE events when portions of the window must be redrawn.

Some display environments have an option for automatically stretching all windows. When this option is enabled, this automatic stretching distorts the appearance of the pygame window. In the pygame examples directory, there is example code (prevent_display_stretching.py) which shows how to disable this automatic stretching of the pygame display on Microsoft Windows (Vista or newer required).

# 这是一级标题
## 这是二级标题
### 这是三级标题
#### 这是四级标题
##### 这是五级标题
###### 这是六级标题

**这是加粗的文字**
*这是倾斜的文字*`
***这是斜体加粗的文字***
~~这是加删除线的文字~~

>这是引用的内容
>>这是引用的内容
>>>>>>>>>>这是引用的内容

---
----
***
*****

![blockchain](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/
u=702257389,1274025419&fm=27&gp=0.jpg "区块链")

[简书](http://jianshu.com)
[百度](http://baidu.com)

- 列表内容
+ 列表内容
* 列表内容

注意：- + * 跟内容之间都要有一个空格

1. 列表内容
2. 列表内容
3. 列表内容

注意：序号跟内容之间要有空格

一级无序列表内容

   二级无序列表内容
   二级无序列表内容
   二级无序列表内容

姓名|技能|排行
--|:--:|--:
刘备|哭|大哥
关羽|打|二哥
张飞|骂|三弟

```
    function fun(){
         echo "这是一句非常牛逼的代码";
    }
    fun();
```

```flow
st=>start: 开始
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
&```
# coding=utf-8
"""
pygame-menu
https://github.com/ppizarror/pygame-menu

MENUBAR
MenuBar class to display menu title.

License:
-------------------------------------------------------------------------------
The MIT License (MIT)
Copyright 2017-2020 Pablo Pizarro R. @ppizarror

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-------------------------------------------------------------------------------
"""

import pygame
import pygame.gfxdraw as gfxdraw
import pygameMenu.controls as _controls

from pygameMenu.utils import make_surface
from pygameMenu.widgets.core.widget import Widget

MENUBAR_MODE_ADAPTATIVE = 1
MENUBAR_MODE_SIMPLE = 2
MENUBAR_MODE_TITLE_ONLY = 3
MENUBAR_MODE_TITLE_ONLY_DIAGONAL = 4
MENUBAR_MODE_NONE = 5
MENUBAR_MODE_UNDERLINE = 6
MENUBAR_MODE_UNDERLINE_TITLE = 7


class MenuBar(Widget):
    """
    MenuBar widget.

    :param label: Title of the Menu
    :type label: basestring
    :param width: Width of the widget, generally width of the Menu
    :type width: int, float
    :param back_box: Draw a back-box button on header
    :type back_box: bool
    :param bgcolor: Color behind the polygon (transparent if not given)
    :type bgcolor: tuple, list
    :param mode: Mode of drawing the bar
    :type mode: int
    :param onchange: Callback when changing the selector
    :type onchange: callable, NoneType
    :param onreturn: Callback when pressing return button
    :type onreturn: callable, NoneType
    :param args: Optional arguments for callbacks
    :param kwargs: Optional keyword-arguments for callbacks
    """

    def __init__(self,
                 label,
                 width,
                 back_box=False,
                 bgcolor=None,
                 mode=MENUBAR_MODE_ADAPTATIVE,
                 onchange=None,
                 onreturn=None,
                 *args,
                 **kwargs):
        assert isinstance(label, str)
        assert isinstance(width, (int, float))
        assert isinstance(back_box, bool)

        # MenuBar has no ID
        super(MenuBar, self).__init__(onchange=onchange,
                                      onreturn=onreturn,
                                      args=args,
                                      kwargs=kwargs)

        self._backbox = back_box
        self._backbox_pos = None  # type: (tuple,None)
        self._backbox_rect = None  # type: (pygame.rect.Rect,None)
        self._bgcolor = bgcolor
        self._label = label
        self._mode = mode
        self._offsetx = 0.0
        self._offsety = 0.0
        self._polygon_pos = None  # type: (tuple,None)
        self._width = width

    def _apply_font(self):
        pass

    # noinspection PyMissingOrEmptyDocstring
    def draw(self, surface):
        self._render()

        if self._bgcolor:
            bg = make_surface(self._width, self._rect.height + 5)
            bg.fill(self._bgcolor)
            surface.blit(bg, self._rect.topleft)

        if len(self._polygon_pos) > 2:
            gfxdraw.filled_polygon(surface, self._polygon_pos, self._font_color)

        if self.mouse_enabled and self._backbox:
            pygame.draw.rect(surface, self._font_selected_color, self._backbox_rect, 1)
            pygame.draw.polygon(surface, self._font_selected_color, self._backbox_pos)

        surface.blit(self._surface,
                     (self._rect.topleft[0] + self._offsetx,
                      self._rect.topleft[1] + self._offsety))

    def get_title(self):
        """
        Return the title of the Menu.

        :return: Title
        :rtype: basestring
        """
        return self._label

    def _render(self):
        # noinspection PyProtectedMember
        menu_prev_condition = not self._menu or not self._menu._top or not self._menu._top._prev

        if not self._render_hash_changed(self._menu.get_id(), self._rect.x, self._rect.y, self._label,
                                         self._font_selected_color, menu_prev_condition):
            return

        self._surface = self._render_string(self._label, self._font_selected_color)
        self._rect.width, self._rect.height = self._surface.get_size()

        if self._mode == MENUBAR_MODE_ADAPTATIVE:
            """
            A-----------------B                  D-E: 25 dx
            |****           x | *0,6 height
            |      D----------C
            F----E/
            """
            a = self._rect.x, self._rect.y
            b = self._rect.x + self._width - 1, self._rect.y
            c = self._rect.x + self._width - 1, self._rect.y + self._rect.height * 0.6
            d = self._rect.x + self._rect.width + 25 + self._offsetx, self._rect.y + self._rect.height * 0.6
            e = self._rect.x + self._rect.width + 5 + self._offsetx, \
                self._rect.y + self._rect.height + self._offsety
            f = self._rect.x, self._rect.y + self._rect.height + self._offsety
            self._polygon_pos = a, b, c, d, e, f
            cross_size = self._rect.height * 0.6
        elif self._mode == MENUBAR_MODE_SIMPLE:
            """
            A-----------------B
            |****           x | *1,0 height
            D-----------------C
            """
            a = self._rect.x, self._rect.y
            b = self._rect.x + self._width - 1, self._rect.y
            c = self._rect.x + self._width - 1, self._rect.y + self._rect.height
            d = self._rect.x, self._rect.y + self._rect.height
            self._polygon_pos = a, b, c, d
            cross_size = self._rect.height
        elif self._mode == MENUBAR_MODE_TITLE_ONLY:
            """
            A-----B
            | *** |          x  *0,6 height
            D-----C
            """
            a = self._rect.x, self._rect.y
            b = self._rect.x + self._rect.width + 5 + self._offsetx, self._rect.y
            c = self._rect.x + self._rect.width + 5 + self._offsetx, \
                self._rect.y + self._rect.height + self._offsety
            d = self._rect.x, self._rect.y + self._rect.height + self._offsety
            self._polygon_pos = a, b, c, d
            cross_size = self._rect.height * 0.6
        elif self._mode == MENUBAR_MODE_TITLE_ONLY_DIAGONAL:
            """
            A--------B
            | **** /          x  *0,6 height
            D-----C
            """
            a = self._rect.x, self._rect.y
            b = self._rect.x + self._rect.width + 25 + self._offsetx, self._rect.y
            c = self._rect.x + self._rect.width + 5 + self._offsetx, \
                self._rect.y + self._rect.height + self._offsety
            d = self._rect.x, self._rect.y + self._rect.height + self._offsety
            self._polygon_pos = a, b, c, d
            cross_size = self._rect.height * 0.6
        elif self._mode == MENUBAR_MODE_NONE:
            """
            A------------------B
             ****             x  *0,6 height
            """
            a = self._rect.x, self._rect.y
            b = self._rect.x + self._width - 1, self._rect.y
            self._polygon_pos = a, b
            cross_size = self._rect.height * 0.6
        elif self._mode == MENUBAR_MODE_UNDERLINE:
            """
             ****           x
            A-----------------B *0,20 height
            D-----------------C
            """
            dy = 3
            a = self._rect.x, self._rect.y + 0.9 * self._rect.height + self._offsety + dy
            b = self._rect.x + self._width - 1, self._rect.y + 0.9 * self._rect.height + self._offsety + dy
            c = self._rect.x + self._width - 1, self._rect.y + self._rect.height + self._offsety + dy
            d = self._rect.x, self._rect.y + self._rect.height + self._offsety + dy
            self._polygon_pos = a, b, c, d
            cross_size = 0.6 * self._rect.height
        elif self._mode == MENUBAR_MODE_UNDERLINE_TITLE:
            """
             ****           x
            A----B             *0,20 height
            D----C
            """
            dy = 3
            a = self._rect.x, self._rect.y + 0.9 * self._rect.height + self._offsety + dy
            b = self._rect.x + self._rect.width + 5 + self._offsetx, self._rect.y + 0.9 * self._rect.height + self._offsety + dy
            c = self._rect.x + self._rect.width + 5 + self._offsetx, self._rect.y + self._rect.height + self._offsety + dy
            d = self._rect.x, self._rect.y + self._rect.height + self._offsety + dy
            self._polygon_pos = a, b, c, d
            cross_size = 0.6 * self._rect.height
        else:
            raise ValueError('invalid menubar mode {0}'.format(self._mode))

        cross_size -= self._offsety + 4
        backbox_x = self._rect.x + self._width - 4 - cross_size
        backbox_y = self._rect.y + 3
        self._backbox_rect = pygame.Rect(backbox_x, backbox_y, cross_size, cross_size)

        if menu_prev_condition:
            # Make a cross for top menu
            self._backbox_pos = (
                (self._backbox_rect.left + 4, self._backbox_rect.top + 4),
                (self._backbox_rect.centerx, self._backbox_rect.centery),
                (self._backbox_rect.right - 4, self._backbox_rect.top + 4),
                (self._backbox_rect.centerx, self._backbox_rect.centery),
                (self._backbox_rect.right - 4, self._backbox_rect.bottom - 4),
                (self._backbox_rect.centerx, self._backbox_rect.centery),
                (self._backbox_rect.left + 4, self._backbox_rect.bottom - 4),
                (self._backbox_rect.centerx, self._backbox_rect.centery),
                (self._backbox_rect.left + 4, self._backbox_rect.top + 4),
            )
        else:
            # Make a back arrow for sub-menus
            self._backbox_pos = (
                (self._backbox_rect.left + 5, self._backbox_rect.centery),
                (self._backbox_rect.centerx, self._backbox_rect.top + 5),
                (self._backbox_rect.centerx, self._backbox_rect.centery - 2),
                (self._backbox_rect.right - 5, self._backbox_rect.centery - 2),
                (self._backbox_rect.right - 5, self._backbox_rect.centery + 2),
                (self._backbox_rect.centerx, self._backbox_rect.centery + 2),
                (self._backbox_rect.centerx, self._backbox_rect.bottom - 5),
                (self._backbox_rect.left + 5, self._backbox_rect.centery)
            )

    def set_title(self, title, offsetx=0, offsety=0):
        """
        Set Menu title.

        :param title: Menu title
        :type title: basestring
        :param offsetx: Offset x-position of title (px)
        :type offsetx: int, float
        :param offsety: Offset y-position of title (px)
        :type offsety: int, float
        :return: None
        """
        assert isinstance(title, str)
        assert isinstance(offsetx, (int, float))
        assert isinstance(offsety, (int, float))
        self._label = title
        self._offsety = offsety
        self._offsetx = offsetx

    # noinspection PyMissingOrEmptyDocstring
    def update(self, events):
        updated = False
        for event in events:  # type: pygame.event.EventType

            if self.mouse_enabled and event.type == pygame.MOUSEBUTTONUP:
                if self._backbox_rect and self._backbox_rect.collidepoint(*event.pos):
                    self.sound.play_click_mouse()
                    self.apply()
                    updated = True

            elif self.joystick_enabled and event.type == pygame.JOYBUTTONDOWN:
                if event.button == _controls.JOY_BUTTON_BACK:
                    self.sound.play_key_del()
                    self.apply()
                    updated = True

        return updated

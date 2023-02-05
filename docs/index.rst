
:orphan:

.. This page is orphan because its content concerns the internal working of the
.. library. However it is necessary in order to be able to quote its items in the
.. documentation.

.. image:: _static/logo.png
    :scale: 35%
    :align: center

.. include:: ../README.rst


===========
First steps
===========

Making games using Unreal Engine is really cool, but when you want to `mod <https://en.wikipedia.org/wiki/Video_game_modding>`_ a game, it can be harder.

To mod a game, you need to extract the game files. To extract the game files, you need Unreal Engine's UnrealPak. To use Unreal Engine's UnrealPak, you need to open it in Windows's CMD.

That's where **UnrealPak-tool** do de job: It can extract a .pak file to a folder that will be chosen by the user. All in one program with a easy-to-use interface.

Here is a tutorial of how to create a menu with **UnrealPak-tool** :

1. Select UnrealPak-tool's version to install

.. image:: ../_static/select_version_to_install.gif
    :align: center
    :alt: Select UnrealPak-tool's version to install
    :width: 600

2. Select UnrealPak-tool's mode to install


.. image:: ../_static/select_mode_to_install.gif
    :align: center
    :alt: Select UnrealPak-tool's mode to install
    :width: 600

**Interested in** :ref:`going deeper into menu design <Creating menus>` **?**

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: First steps

    _source/create_menu
    _source/add_widgets
    _source/add_sounds
    _source/themes
    _source/gallery


==============
Advanced usage
==============

This chapter define rules and advanced tips and tricks to develop extensions for
:py:mod:`pygame-menu`. The main addressed topics are:

- :ref:`Creating a widget <Create a widget>`
- :ref:`Creating a selection effect <Create a selection effect>`

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Advanced usage

    _source/advanced
    _source/advanced_controller
    _source/advanced_selection

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Menu APIs

    _source/baseimage
    _source/scrollarea.rst


===========
Widgets API
===========

A menu is in fact a list of widgets arranged on the same surface.
Access to a widget in a menu can easily be done with two methods:

.. code-block:: python

    widget = menu.get_widget('MyWidgetID')

    selected = menu.get_selected_widget()

Each :py:mod:`pygame_menu` widget and its behaviors are defined in a
class. The currently existing classes are:

    - :py:class:`~pygame_menu.widgets.Button`
    - :py:class:`~pygame_menu.widgets.ColorInput`
    - :py:class:`~pygame_menu.widgets.DropSelect`
    - :py:class:`~pygame_menu.widgets.DropSelectMultiple`
    - :py:class:`~pygame_menu.widgets.Frame`
    - :py:class:`~pygame_menu.widgets.HMargin`
    - :py:class:`~pygame_menu.widgets.Image`
    - :py:class:`~pygame_menu.widgets.Label`
    - :py:class:`~pygame_menu.widgets.MenuBar`
    - :py:class:`~pygame_menu.widgets.MenuLink`
    - :py:class:`~pygame_menu.widgets.NoneWidget`
    - :py:class:`~pygame_menu.widgets.ProgressBar`
    - :py:class:`~pygame_menu.widgets.RangeSlider`
    - :py:class:`~pygame_menu.widgets.ScrollBar`
    - :py:class:`~pygame_menu.widgets.Selector`
    - :py:class:`~pygame_menu.widgets.SurfaceWidget`
    - :py:class:`~pygame_menu.widgets.Table`
    - :py:class:`~pygame_menu.widgets.TextInput`
    - :py:class:`~pygame_menu.widgets.ToggleSwitch`
    - :py:class:`~pygame_menu.widgets.VFill`
    - :py:class:`~pygame_menu.widgets.VMargin`

For advanced programmers, those classes can be used to design custom menus or windows.

Have a look at `pygame_menu.widgets.examples.scrollbar.py <https://github.com/ppizarror/pygame-menu/tree/master/pygame_menu/widgets/examples/scrollbar.py>`_ for
instance. It shows how to use the :py:class:`pygame_menu.widgets.ScrollBar` class
to display large custom surfaces.

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Widgets API

    _source/widgets_button
    _source/widgets_colorinput
    _source/widgets_dropselect
    _source/widgets_dropselect_multiple
    _source/widgets_frame
    _source/widgets_hmargin
    _source/widgets_image
    _source/widgets_label
    _source/widgets_menubar
    _source/widgets_menulink
    _source/widgets_none
    _source/widgets_progressbar
    _source/widgets_rangeslider
    _source/widgets_scrollbar
    _source/widgets_selector
    _source/widgets_surface
    _source/widgets_table
    _source/widgets_textinput
    _source/widgets_toggleswitch
    _source/widgets_vfill
    _source/widgets_vmargin


=================
About pygame-menu
=================

This project does not have a mailing list and so the issues tab should be the first
point of contact if wishing to discuss the project. If you have questions that you
do not feel are relevant to the issues tab or just want to let me know what you
think about the library, feel free to email me at pablo@ppizarror.com

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: About pygame-menu

    _source/license
    _source/contributors


==================
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Migration Guides

    _source/migration_guide_2_to_3
    _source/migration_guide_3_to_4

import wx


def create_board(frame, tile_size):
    x_pos_list = range(0, tile_size[0] * 7, tile_size[0])
    y_pos_list = range(0, tile_size[1] * 7, tile_size[1])

    colors = [wx.Colour(red=255, green=255, blue=255), wx.Colour(red=0, green=0, blue=0)]
    colors = ["white", "black"]
    color_ind = 0
    for x_pos in x_pos_list:
        for y_pos in y_pos_list:
            panel = wx.Panel(frame, pos=(x_pos, y_pos), size=tile_size)
            panel.SetBackgroundColour(colors[color_ind])

            if color_ind == 0:
                color_ind = 1
            else:
                color_ind = 0



app = wx.App()

frame = wx.Frame(None, size=(30 * 8, 30 * 9),  title="Test Test 123")

create_board(frame, (30, 30))

frame.Show()

app.MainLoop()



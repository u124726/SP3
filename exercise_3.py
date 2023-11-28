import subprocess


# BBB grayscale conversion
def grayscale():
    """ Converts Big Buck Bunny video to grayscale using ffmpeg """

    ffmpeg_bw = [
        'ffmpeg',
        '-i', 'BBB.mp4',
        '-vf', f'format=gray',
        '/mnt/c/Users/dcabo/PycharmProjects/SP3/BBB_bw.mp4'
    ]
    subprocess.run(ffmpeg_bw)


# BBB 360x240 resize conversion
def size():
    """ Resize BBB video with new dimension 360x240"""

    ffmpeg_size = [
        'ffmpeg',
        '-i', 'BBB.mp4',
        '-vf', f'scale={360}:{240}',
        '/mnt/c/Users/dcabo/PycharmProjects/SP3/BBB_size.mp4'
    ]
    subprocess.run(ffmpeg_size)


# BBB histogram in real time conversion
def yuv_hist():
    """ Extract YUV histogram from an input video and outputs another one with histogram displayed"""

    ffmpeg_yh = [
        'ffmpeg',
        '-i', 'BBB.mp4',
        '-vf', f'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay',
        '/mnt/c/Users/dcabo/PycharmProjects/SP3/BBB_yv.mp4'
    ]
    subprocess.run(ffmpeg_yh)


# BBB macro-blocks and motion vectors
def macro_and_motion():
    """ Creates a new video from Big Buck Bunny video which show macro blocks and motion vectors using ffmpeg"""

    ffmpeg_mm = [
        'ffmpeg',
        '-flags2',
        '+export_mvs',
        '-i', 'BBB.mp4',
        '-vf', f'codecview=mv=pf+bf+bb',
        '/mnt/c/Users/dcabo/PycharmProjects/SP3/BBB_yv.mp4'
    ]
    subprocess.run(ffmpeg_mm)

import subprocess


def comparison(input_video1, input_video2, output_video):
    """ Creates video comparison between two input videos
        Args:
            input_video1: First video to compare
            input_video2: Second video to compare
            output_video: New video comparing two input videos
    """
    ffmpeg_comp = [
        'ffmpeg',
        '-i', input_video1,
        '-i', input_video2,
        '-filter_complex', f'blend=all_mode=difference',
        '-crf', f'18',
        output_video
    ]

    subprocess.run(ffmpeg_comp)


comparison('BBB.mp4', 'BBB_grayscale.mp4',  '/mnt/c/Users/dcabo/PycharmProjects/SP3/video_comparison.mp4')
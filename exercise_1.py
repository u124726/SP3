import subprocess
import exercise_2


class Codecs:

    # EXERCISE 1
    def resolution_size(input_video, output_resolution, output_size):
        """ Creates 2 videos with new resolution 720p or size 360x240 from Big Buck Bunny video
            Args:
                input_video: Big Buck Bunny video
                output_resolution: New video with resolution 720p
                output_size: New video with size 360x240
        """
        ffmpeg_resolution = [
            'ffmpeg',
            '-i', input_video,
            '-vf', f'scale={-1}:{720}',
            output_resolution
        ]

        ffmpeg_size = [
            'ffmpeg',
            '-i', input_video,
            '-vf', f'scale={360}:{240}',
            output_size
        ]

        subprocess.run(ffmpeg_resolution)
        subprocess.run(ffmpeg_size)

    def codec_conversion(input_video, output_h265, output_av1):
        """ Convert Big Buck Bunny video using AV1 y H.265 codecs
            Args:
                input_video: Big Buck Bunny video
                output_h265: New video with H.265 conversion
                output_av1: New video with AV1 conversion
        """
        ffmpeg_h265 = [
            'ffmpeg',
            '-i', input_video,
            '-crf', f'26',
            '-preset', f'fast',
            '-b:a', f'128k',
            output_h265
        ]

        ffmpeg_av1 = [
            'ffmpeg',
            '-i', input_video,
            '-crf', f'30',
            output_av1
        ]

        subprocess.run(ffmpeg_h265)
        subprocess.run(ffmpeg_av1)

    #resolution_size('BBB.mp4', '/mnt/c/Users/dcabo/PycharmProjects/SP3/BBB_720p.mp4', '/mnt/c/Users/dcabo/PycharmProjects/SP3/BBB_resize.mp4')
    #codec_conversion('BBB.mp4', '/mnt/c/Users/dcabo/PycharmProjects/SP3/video_h265.mp4', '/mnt/c/Users/dcabo/PycharmProjects/SP3/video_av1.mkv')

    # EXERCISE 2
    codec_conversion('video_comparison.mp4', '/mnt/c/Users/dcabo/PycharmProjects/SP3/video_h265.mp4', '/mnt/c/Users/dcabo/PycharmProjects/SP3/video_av1.mkv')

    """Podemos observar que existe una diferencia de tamaño de nuestro video_comparison.mp4 cuando aplicamos un codec
    AV1 o H.265, en el primer caso el tamaño es de 8468KB mientras que para el H.265 es de 11549KB, por lo que vemos 
    una mayor eficiencia en términos de compresión con codec AV1"""
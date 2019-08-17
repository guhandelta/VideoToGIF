# Installed Python's imageio library's imageio-ffmpeg package to convert a short videoclip to GIF image
import imageio
import os

clip = os.path.abspath('breakfast.mp4') # Gets the path of the video file specified in the fn()

def gifMaker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat
    # os.path.splitext gives the output as ('breakfast','.mp4'), os.path.splitext(inputPath)[0] => is specified here to get the 'breakfast'
    # the + targetFormat will add the specified format, which in this case would be a GIF format

    print(f'Converting {inputPath} \n to {outputPath}')

    reader = imageio.get_reader(inputPath) # Specifying the path of the video clip for the imageio library to read

    # Can mention any required FPS for the GIF here, but in this case, am specifying to take the FPS of the video
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader: # Reading the video and extracting all the frames
        writer.append_data(frames) # Writing it to the writer to ceate the GIF
        print(f'Frame {frames}')
    print('GIF Ready!!')
    writer.close()

gifMaker(clip,'.gif')
    




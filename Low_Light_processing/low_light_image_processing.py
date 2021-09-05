import logging

import cv2
import click
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)


class LongExposure:
    def __init__(self, video, output_image_path, step=1):
        self.video = video
        self.output_image_path = output_image_path
        self.step = step

    @staticmethod
    def averager():
        
        count = 0
        total = 0.0

        def average(value,reset,step):
            nonlocal count, total
            if reset:
                total = 0.0
            count += 1
            total += value
            return total / 2
        return average

    def __call__(self):
        logging.info("Processing video %r with step %r", self.video, self.step)

        
        stream = cv2.VideoCapture(self.video)

        
        total_frames = int(stream.get(cv2.CAP_PROP_FRAME_COUNT))

        r, g, b = None, None, None
        r_avg, g_avg, b_avg = self.averager(), self.averager(), self.averager()

        _, frame = stream.read()
        height, width, channels = frame.shape

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(self.output_image_path, fourcc, 5.0, (width, height))

        for count in tqdm(range(total_frames)):
            _, frame = stream.read()
            b_curr, g_curr, r_curr = cv2.split(frame.astype("float"))
            r, g, b = r_avg(r_curr,False,self.step), g_avg(g_curr,False,self.step), b_avg(b_curr,False,self.step)
            avg = cv2.merge([b, g, r]).astype("uint8")
            if count % self.step == 0 and frame is not None:
                
                
                # logging.info("Saving image as %r", str(count)+self.output_image_path)
                # cv2.imwrite(str(count)+self.output_image_path, avg)
                out.write(avg)
                avg = None
                r, g, b = r_avg(r_curr,True,self.step), g_avg(g_curr,True,self.step), b_avg(b_curr,True,self.step)
                r, g, b = None, None, None
        stream.release()
        out.release()


@click.group()
def cli():
    pass


@cli.command()
@click.argument("video_path", nargs=1, type=str)
@click.argument("image_path", nargs=1, type=str)
@click.option(
    "--step",
    "-s",
    default=1,
    type=int,
    show_default=True,
    help="Step used to get the frames.",
)
def local_video(video_path, image_path, step):
    
    long_exposure = LongExposure(video_path, image_path, step)
    long_exposure()


@cli.command()
@click.argument("video_link", nargs=1, type=str)
@click.argument("image_path", nargs=1, type=str)
@click.option(
    "--step",
    "-s",
    default=1,
    type=int,
    show_default=True,
    help="Step used to get the frames.",
)
def youtube_video(video_link, image_path, step):
    raise NotImplementedError("Not implemented yet")


if __name__ == "__main__":
    # cli()
    long_exposure = LongExposure("./clip1.mp4", "./output.mp4", 3)
    long_exposure()

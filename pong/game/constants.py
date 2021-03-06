import os

MAX_X = 825
MAX_Y = 625
MAX_Y_HALF = 300
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 90
DEFAULT_TEXT_OFFSET = 4

# IMAGE_BRICK = os.path.join(os.getcwd(), "cse210-batter\\batter\\assets\\brick-3.png")
# IMAGE_PADDLE = os.path.join(os.getcwd(), "cse210-batter\\batter\\assets\\bat.png")
# IMAGE_BALL = os.path.join(os.getcwd(), "cse210-batter\\batter\\assets\\ball.png")

# SOUND_START = os.path.join(os.getcwd(), "cse210-batter\\batter\\assets\start.wav")
# SOUND_BOUNCE = os.path.join(os.getcwd(), "cse210-batter\\batter\\assets\\boing.wav")
# SOUND_OVER = os.path.join(os.getcwd(), "cse210-batter\\batter\\assets\over.wav")

SOUND_PADDLE_BOUNCE = os.path.join(os.getcwd(), "CSE_210_Final\\pong\\assets\\off paddle sound.wav")
SOUND_START = os.path.join(os.getcwd(), "CSE_210_Final\\pong\\assets\\start sound.wav")
SOUND_END = os.path.join(os.getcwd(), "CSE_210_Final\\pong\\assets\\game over sound.wav")
SOUND_HIT = os.path.join(os.getcwd(), "CSE_210_Final\\pong\\assets\\hit sound.wav")

IMAGE_BALL = os.path.join(os.getcwd(), "CSE_210_Final\\pong\\assets\\ball for pong.png")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX * -1

PADDLE_X = MAX_X / 2
PADDLE_Y = MAX_Y - 25

SCORE_HEIGHT = 50
SCORE_WIDTH = 40

# BRICK_WIDTH = 24
# BRICK_HEIGHT = 48

# BRICK_SPACE = 5

PADDLE_SPEED = 15

PADDLE_WIDTH = 24
PADDLE_HEIGHT = 100

BALL_WIDTH = 24
BALL_HEIGHT = 24


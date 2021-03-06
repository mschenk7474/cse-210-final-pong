import os
os.environ['RAYLIB_BIN_PATH'] = r'cse210-batter\batter\game\raylib-2.0.0-Win64-mingw\lib'

import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService


# from game.brick import Brick
from game.ball import Ball
from game.paddles import Paddles
from game.score_board import ScoreBoard
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction
from game.check_end import CheckEnd

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    #CREATE BALL AND PADDLES HERE

    cast["ball"] = []
    ball = Ball()
    ball.set_ball()
    ball = ball.get_ball()
    cast["ball"] = ball

    cast["paddleL"] = []
    paddleL = Paddles()
    paddleL.set_paddle_left()
    paddleL = paddleL.get_paddle_left()
    cast["paddleL"] = paddleL

    cast["paddleR"] = []
    paddleR = Paddles()
    paddleR.set_paddle_right()
    paddleR = paddleR.get_paddle_right()
    cast["paddleR"] = paddleR

    cast["scoreboardL"] = []
    scoreL = ScoreBoard()
    scoreL.set_scoreboard_left()
    scoreL = scoreL.get_scoreboard_left()
    cast["scoreboardL"] = scoreL

    cast["scoreboardR"] = []
    scoreR = ScoreBoard()
    scoreR.set_scoreboard_right()
    scoreR = scoreR.get_scoreboard_right()
    cast["scoreboardR"] = scoreR

   #  cast["bricks"] = []
   #  brick = Brick()
   #  brick.set_brick()
   #  bricks = brick.get_bricks()
   #  cast["bricks"] = bricks

   #  cast["balls"] = []
   #  ball = Ball()
   #  ball.set_ball()
   #  ball = ball.get_ball()
   #  cast["balls"] = ball

   #  cast["paddle"] = []
   #  paddle = Paddle()
   #  paddle.set_paddle()
   #  paddle = paddle.get_paddle()
   #  cast["paddle"] = paddle



    # Create the script {key: tag, value: list}
    script = {}

   # THIS IS WHERE THE ACTORS ARE MADE TO DO THEIR THINGS ON SCREEN

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)
    check_end = CheckEnd(cast)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action, handle_off_screen_action]
    script["output"] = [check_end, draw_actors_action]  
   #  script["input"] = [control_actors_action]
   #  script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action]
   #  script["output"] = [check_end, draw_actors_action]



    # Start the game
    output_service.open_window("Pong")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()

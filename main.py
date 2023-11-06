import discord
from discord import app_commands

import bombballActions as actions
import logger

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="hit", description="roll to hit")
async def hitRoll(
  interaction: discord.Interaction, 
  hitterStrength: int,
  targetStrength: int,
  numAllies: int,
  numOpponents: int,
):
    roll_result = actions.Hit.roll(hitterStrength, targetStrength, numAllies, numOpponents)
    logger.log(interaction.user.name + "/n" + roll_result)
    await interaction.response.send_message(roll_result)

@tree.command(name="sample_hit", description="get the probabilities for a hit")
async def sampleHitRoll(
  interaction: discord.Interaction, 
  hitterStrength: int,
  targetStrength: int,
  numAllies: int,
  numOpponents: int,
):
    roll_results = actions.Hit.sample_roll(hitterStrength, targetStrength, numAllies, numOpponents)
    await interaction.response.send_message(roll_results)

@tree.command(name="dodge", description="roll to dodge")
async def dodgeRoll(
  interaction: discord.Interaction,
  adj_ops_with_higher_dex: int, 
  adj_ops_with_equal_dex: int,
):
  roll_result = actions.Dodge.roll(adj_ops_with_higher_dex, adj_ops_with_equal_dex)
  logger.log(interaction.user.name + "/n" + roll_result)
  await interaction.response.send_message(roll_result)

@tree.command(name="sample_dodge", description="get the probabilities of a dodge")
async def sampleDodgeRoll(
  interaction: discord.Interaction,
  adj_ops_with_higher_dex: int, 
  adj_ops_with_equal_dex: int,
):
  roll_resulta = actions.Dodge.sample_roll(adj_ops_with_higher_dex, adj_ops_with_equal_dex)
  await interaction.response.send_message(roll_results)

tree.add_command(dodgeRoll)
tree.add_command(sampleDodgeRoll)

@tree.command(name="stumble", description="roll to stumble")
async def stumbleRoll(interaction: discord.Interaction):
  roll_result = actions.Stumble.roll()
  logger.log(interaction.user.name + "/n" + roll_result)
  await interaction.response.send_message(roll_result)

@tree.command(name="sample_stumble", description="get the probabilities of a stumble")
async def sampleStumbleRoll(interaction: discord.Interaction):
  roll_results = actions.Stumble.sample_roll()
  await interaction.response.send_message(roll_results)

tree.add_command(stumbleRoll)
tree.add_command(sampleStumbleRoll)

@tree.command(name="fall", description="roll to fall")
async def fallRoll(interaction: discord.Interaction):
  roll_result = actions.Fall.roll()
  logger.log(interaction.user.name + "/n" + roll_result)
  await interaction.response.send_message(roll_result)

@tree.command(name="sample_fall", description="get probabilities of a fall")
async def sampleFallRoll(interaction: discord.Interaction):
  roll_results = actions.Fall.sample_roll()
  await interaction.response.send_message(roll_results)

tree.add_command(fallRoll)
tree.add_command(sampleFallRoll)

@tree.command(name="throw", descripition="roll to throw")
async def throwRoll(interaction: discord.Interaction, thrower_dex):
  roll_result = actions.Throw.roll(thrower_dex)
  logger.log(interaction.user.name + "/n" + roll_result)
  await interaction.response.send_message(roll_result)

@tree.command(name="sample_throw", descripition="get probabilities for a throw")
async def sampleThrowRoll(interaction: discord.Interaction, thrower_dex):
  roll_results = actions.Throw.sample_roll(thrower_dex)
  await interaction.response.send_message(roll_results)

tree.add_command(throwRoll)
tree.add_command(sampleThrowRoll)

@tree.command(name="block_pass", description="roll to block a pass")
async def blockPassRoll(
  interaction: discord.Interaction, 
  blocker_dex: int, 
  num_additional_blockers: int
):
  roll_result = actions.PassBlock.roll(blocker_dex, num_additional_blockers)
  logger.log(interaction.user.name + "/n" + roll_result)
  await interaction.response.send_message(roll_result)

@tree.command(name="sample_block_pass", description="get the probabilities for blocking a pass")
async def sampleBlockPassRoll(
  interaction: discord.Interaction, 
  blocker_dex: int, 
  num_additional_blockers: int
):
  roll_results = actions.PassBlock.sample_roll(blocker_dex, num_additional_blockers)
  await interaction.response.send_message(roll_results)

tree.add_command(blockPassRoll)
tree.add_command(sampleBlockPassRoll)

@tree.command(name="catch", description="roll to catch")
async def catchRoll(
  interaction: discord.Interaction,
  catchers_dex: int, 
  num_opposing_players: int, 
  catch_bonus: int
):
  roll_result = actions.Catch.roll(catchers_dex, num_opposing_players, catch_bonus)
  logger.log(interaction.user.name + "/n" + roll_result)
  await interaction.response.send_message(roll_result)

@tree.command(name="sample_catch", description="get the probabilities for catching")
async def sampleCatchRoll(
  interaction: discord.Interaction,
  catchers_dex: int, 
  num_opposing_players: int, 
  catch_bonus: int
):
  roll_results = actions.Catch.sample_roll(catchers_dex, num_opposing_players, catch_bonus)
  await interaction.response.send_message(roll_results)

tree.add_command(catchRoll)
tree.add_command(sampleCatchRoll)

@tree.command(name="hold_ball", description="roll to hold ball")
async def holdBallRoll(interaction: discord.Interaction, holders_dex: int):
  roll_result = actions.HoldBall.roll(holders_dex)
  logger.log(interaction.user.name + "/n" + roll_result)
  await interaction.response.send_message(roll_result)

@tree.command(name="sample_hold_ball", description="get the probabilities for holding ball")
async def sampleHoldBallRoll(interaction: discord.Interaction, holders_dex: int):
  roll_results = actions.HoldBall.sample_roll(holders_dex)
  await interaction.response.send_message(roll_results)

tree.add_command(holdBallRoll)
tree.add_command(sampleHoldBallRoll)

@tree.command(name="ball_scatter_roll", descripition="roll to scatter ball")
async def ballScatterRoll(interaction: discord.Interaction):
  roll_result = actions.BallScatter.roll()
  logger.log(interaction.user.name + "/n" + roll_result)
  await interaction.response.send_message(roll_result)

tree.add_command(ballScatterRoll)

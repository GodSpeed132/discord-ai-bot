from google import genai
from google.genai import types 
from discord.ext import commands
import sqlite3


class convo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = genai.Client()
        self.connection = sqlite3.connect('discdb.db')


    @commands.command()
    async def chat(self, ctx, *, question):
        
        try:
            response = self.client.models.generate_content(model="gemini-2.5-flash", 
                                                           contents=question, 
                                                           config=types.GenerateContentConfig(system_instruction="you're a bot in the great CML server"))

            try:
                cursor = self.connection.cursor()
                cursor.execute('INSERT INTO conversations (user_id, question, answer) VALUES (?, ?, ?)', 
                            (str(ctx.author.id), question, response.text))
                self.connection.commit()
            except Exception as db_error:
                print(f"DB Error: {db_error}")

            await ctx.send(response.text)

        except Exception as e:
            print(f'Error occured: {e}')
            await ctx.send("Error happened")
    


    @commands.command()
    async def history(self, ctx):
        try: 
            cursor = self.connection.cursor()
            cursor.execute('SELECT question, answer FROM conversations WHERE user_id = ? ORDER BY id DESC LIMIT 5', (str(ctx.author.id),))

            db_response = cursor.fetchall()

            if not db_response:  # or: if db_response == []
                await ctx.send("You have no conversation history yet!")
                return

            
            formatted = "\n\n".join([f"**Q:** {row[0][:100]}...\n**A:** {row[1][:300]}..." 
                                  for row in db_response])
            

            await ctx.send(formatted)

        except Exception as e:
            print(f"Error getting history for user{e}")
            await ctx.send(f"Error occured and could not fetch history for {str(ctx.author.id)}")


    @commands.command()
    async def clear_history(self, ctx):
        try: 
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM conversations WHERE user_id = ?', (str(ctx.author.id),))
            self.connection.commit()

            await ctx.send(f'history deleted for {str(ctx.author.id)}')

        except Exception as e:
            print(f"Error deleting history for user{e}")
            await ctx.send(f"Error occured and could not delete history for {str(ctx.author.id)}")

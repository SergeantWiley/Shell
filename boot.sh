read -p "Want to play some RPS?: " entry
# Check the user's input
if [ "$entry" = "yes" ]; then
    python game.py
else
    echo "Dang, Not today I guess."
fi
read -p "Press Enter to exit..."
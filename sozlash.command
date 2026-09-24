#!/bin/bash
# Mac uchun: Claude Code buyruqlarini (.claude papkasi) o'rnatadi. Bir marta bosilsa yetarli.
cd "$(dirname "$0")" || exit 1

[ -d ".claude" ] || cp -R "_claude" ".claude"
echo "Claude Code sozlamalari tayyor (.claude papkasi)."
echo
read -r -p "Yopish uchun Enter bosing..." _

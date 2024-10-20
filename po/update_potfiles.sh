#!/bin/bash

version=$(fgrep "version: " ../meson.build | grep -v "meson" | grep -o "'.*'" | sed "s/'//g")

find ../LiteUtils -iname "*.py" | xargs xgettext --package-name=LiteUtils --package-version=$version --from-code=UTF-8 --output=liteutils-python.pot
find ../data/ui -iname "*.blp" | xargs xgettext --package-name=LiteUtils --package-version=$version --from-code=UTF-8 --output=liteutils-blueprint.pot -L Python --keyword=C_:1c,2
find ../data/ -iname "*.desktop.in" | xargs xgettext --package-name=LiteUtils --package-version=$version --from-code=UTF-8 --output=liteutils-desktop.pot -L Desktop

msgcat --sort-by-file --use-first --output-file=liteutils.pot liteutils-python.pot liteutils-blueprint.pot liteutils-desktop.pot

sed 's/#: //g;s/:[0-9]*//g;s/\.\.\///g' <(fgrep "#: " liteutils.pot) | sed s/\ /\\n/ | sort | uniq > POTFILES.in

echo "# Please keep this list alphabetically sorted" > LINGUAS
for l in $(ls *.po); do basename $l .po >> LINGUAS; done

for lang in $(sed "s/^#.*$//g" LINGUAS); do
    mv "${lang}.po" "${lang}.po.old"
    msginit --no-translator --locale=$lang --input liteutils.pot
    mv "${lang}.po" "${lang}.po.new"
    msgmerge -N "${lang}.po.old" "${lang}.po.new" > ${lang}.po
    rm "${lang}.po.old" "${lang}.po.new"
done

rm liteutils-*.pot

# To create language file use this command
# msginit --locale=LOCALE --input liteutils.pot
# where LOCALE is something like de, it, es...

# To compile a .po file
# msgfmt --output-file=xx.mo xx.po
# where xx is something like de, it, es...

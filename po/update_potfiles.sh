#!/bin/bash

version=$(fgrep "version: " ../meson.build | grep -v "meson" | grep -o "'.*'" | sed "s/'//g")

find ../LwUtils -iname "*.py" | xargs xgettext --package-name=LwUtils --package-version=$version --from-code=UTF-8 --output=lwutils-python.pot
find ../data/ui -iname "*.blp" | xargs xgettext --package-name=LwUtils --package-version=$version --from-code=UTF-8 --output=lwutils-blueprint.pot -L Python --keyword=C_:1c,2
find ../data/ -iname "*.desktop.in" | xargs xgettext --package-name=LwUtils --package-version=$version --from-code=UTF-8 --output=lwutils-desktop.pot -L Desktop

msgcat --sort-by-file --use-first --output-file=lwutils.pot lwutils-python.pot lwutils-blueprint.pot lwutils-desktop.pot

sed 's/#: //g;s/:[0-9]*//g;s/\.\.\///g' <(fgrep "#: " lwutils.pot) | sed s/\ /\\n/ | sort | uniq > POTFILES.in

echo "# Please keep this list alphabetically sorted" > LINGUAS
for l in $(ls *.po); do basename $l .po >> LINGUAS; done

for lang in $(sed "s/^#.*$//g" LINGUAS); do
    mv "${lang}.po" "${lang}.po.old"
    msginit --no-translator --locale=$lang --input lwutils.pot
    mv "${lang}.po" "${lang}.po.new"
    msgmerge -N "${lang}.po.old" "${lang}.po.new" > ${lang}.po
    rm "${lang}.po.old" "${lang}.po.new"
done

rm lwutils-*.pot

# To create language file use this command
# msginit --locale=LOCALE --input lwutils.pot
# where LOCALE is something like de, it, es...

# To compile a .po file
# msgfmt --output-file=xx.mo xx.po
# where xx is something like de, it, es...

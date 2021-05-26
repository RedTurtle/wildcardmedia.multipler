.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
wildcardmedia.multipler
==============================================================================

Multipler adapter for the "new" wildcard.media product (from version 3.x).

Features
--------

- This product gives the 'new' wildcard.media the support for videos uploaded on
  the Multipler service.


Valid URL format
================

    https://multipler.lepida.it/assemblealegislativa1/video/...


Poster Images for the html5 video tag
=====================================

[update 2018]

Il player multipler non è altro che un normalissimo tag `video` html5, quindi
è il browser che decide come mostrarti il player.

Il tag `video` html5 ha un attributo `poster` che permette di specificare una
immagine che faccia da cover al video prima che venga riprodotto.

Multipler ora genera in automatico le immagini da usare come poster e sono
disponibili all'URL in questo formato:

    https://multipler.lepida.it/assemblealegislativa1/video/thumbs/assemblealegislativa1_XXXX.jpg


dove XXXX è il codice identificativo del video che ha come url:

    https://multipler.lepida.it/assemblealegislativa1/video/thumbs/assemblealegislativa1_XXXX.jpg


L'immagine impostata direttamente sul contenuto nel campo `image` ha la
precedenza sul poster generato da multipler. Questo per evitare problemi dati
da miniature generate con snapshot totalmente neri.

test-multipler.lepida.it
========================

C'è un adapter speicifico per l'ambiente di test di Multipler per testare i nuovi player con un template ad hoc (sperimentale).

Installation
------------

Install wildcardmedia.multipler by adding it to your buildout::

    [buildout]

    ...

    eggs =
        wildcardmedia.multipler


and then running ``bin/buildout``


When finished, you can now add a new Video content with a Multipler URL in the
``Video URL`` field and use it in your website.


Contribute
----------

- Issue Tracker: https://github.com/collective/wildcardmedia.multipler/issues
- Source Code: https://github.com/collective/wildcardmedia.multipler
- Documentation: https://docs.plone.org/foo/bar


License
-------

The project is licensed under the GPLv2.

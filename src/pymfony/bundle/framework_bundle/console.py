# -*- coding: utf-8 -*-
# This file is part of the pymfony package.
#
# (c) Alexandre Quercia <alquerci@email.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from __future__ import absolute_import;

from pymfony.component.system.exception import InvalidArgumentException
from pymfony.component.system import ReflectionClass
from pymfony.bundle.framework_bundle.controller import ControllerNameParser as BaseControllerNameParser

"""
"""

class ControllerNameParser(BaseControllerNameParser):
    """ControllerNameParser converts command from the short notation a:b:c
    (BlogBundle:Post:index) to a fully-qualified class.method string:
    (Bundle.BlogBundle.Command.PostCommand.indexAction).

    @author: Fabien Potencier <fabien@symfony.com>

    """

    def parse(self, controller):
        """Converts a short notation a:b:c to a class.method.

        @param: string controller A short notation controller (a:b:c)

        @return string A string with class.method

        @raise InvalidArgumentException when the specified bundle is not enabled:
                                          or the controller cannot be found

        """
        parts = controller.split(':');
        if (3  != len(parts)) :
            raise InvalidArgumentException(
                'The "{0}" controller is not a valid a:b:c controller string.'
                ''.format(controller)
            );


        bundle, controller, action = parts;
        controller = controller.replace('/', '.');
        bundles = list();

        # this raise an exception if there is no such bundle:
        for b in self._kernel.getBundle(bundle, False):
            test = b.getNamespace()+'.command.'+controller+'Command';
            if ReflectionClass(test).exists() :
                return test+'::'+action+'Action';


            bundles.append(b.getName());
            msg = (
                'Unable to find command "{0}:{1}" - class "{2}" does not '
                'exist.'.format(
                    bundle,
                    controller,
                    test,
            ));


        if (len(bundles) > 1) :
            msg = (
                'Unable to find command "{0}:{1}" in bundles {2}.'
                ''.format(
                    bundle,
                    controller,
                    ', '.join(bundles)
            ));


        raise InvalidArgumentException(msg);
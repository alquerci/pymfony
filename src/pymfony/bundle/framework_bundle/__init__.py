# -*- coding: utf-8 -*-
# This file is part of the pymfony package.
#
# (c) Alexandre Quercia <alquerci@email.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from __future__ import absolute_import;

from pymfony.component.kernel.bundle import Bundle;

from pymfony.component.dependency import ContainerBuilder;
from pymfony.component.dependency import Scope;
from pymfony.component.dependency.compiler import PassConfig;

from pymfony.bundle.framework_bundle.dependency.compiler import RegisterKernelListenersPass;
from pymfony.bundle.framework_bundle.dependency.compiler import ConsoleRoutingResolverPass;
from pymfony.bundle.framework_bundle.dependency.compiler import AddCacheWarmerPass;
from pymfony.bundle.framework_bundle.dependency.compiler import AddCacheClearerPass;
from pymfony.bundle.framework_bundle.dependency.compiler import CompilerDebugDumpPass;

from pymfony.component.console_routing import RouteCollection;
from pymfony.component.console_routing import Route;

from pymfony.component.console.input import InputArgument;
from pymfony.component.console.input import InputOption;

"""
Pymfony FrameworkBundle
"""

class FrameworkBundle(Bundle):
    """Bundle.

    @author: Fabien Potencier <fabien@symfony.com>

    """

    def build(self, container):
        assert isinstance(container, ContainerBuilder);

        Bundle.build(self, container);

        container.addScope(Scope('request'));

        container.addCompilerPass(ConsoleRoutingResolverPass());
        container.addCompilerPass(RegisterKernelListenersPass(), PassConfig.TYPE_AFTER_REMOVING);
        container.addCompilerPass(AddCacheWarmerPass());
        container.addCompilerPass(AddCacheClearerPass());

        if container.getParameter('kernel.debug') :
            container.addCompilerPass(CompilerDebugDumpPass(), PassConfig.TYPE_AFTER_REMOVING);


    def registerCommands(self, collection):
        assert isinstance(collection, RouteCollection);

        collection\
            .add('framework_list', Route("list", "Lists commands", {
                '_controller': "FrameworkBundle:List:show",
            }, [
                InputArgument('namespace', InputArgument.OPTIONAL, 'The namespace name'),
                InputOption('raw', None, InputOption.VALUE_NONE, 'To output raw command list'),
            ]))\
            .add('framework_version', Route("_fragment:framework:version", "Show application version", {
                '_controller': "FrameworkBundle:Version:long",
            }))\
            .add('framework_help', Route("help", "Displays help for a command", {
                '_controller': "FrameworkBundle:Help:show",
            }, [
                InputArgument('command_name', InputArgument.OPTIONAL, 'The command name', 'help'),
                InputOption('xml', None, InputOption.VALUE_NONE, 'To output help as XML'),
            ]))\
            .add('framework_cache_clear', Route('cache:clear', 'Clears the cache', {
                '_controller': "FrameworkBundle:Cache:clear",
            }, [
                InputOption('no-warmup', '', InputOption.VALUE_NONE, 'Do not warm up the cache'),
                InputOption('no-optional-warmers', '', InputOption.VALUE_NONE, 'Skip optional cache warmers (faster)'),
            ]))\
            .add('framework_cache_warmup', Route('cache:warmup', 'Warms up an empty cache', {
                '_controller': "FrameworkBundle:Cache:warmup",
            }, [
                InputOption('no-optional-warmers', '', InputOption.VALUE_NONE, 'Skip optional cache warmers (faster)'),
            ]))\
        ;

define(
    ['text!../contentNewStrategyTargeting/view.html', 'strategy'],
    function(template, strategy) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = strategy.strategyVM;

        this.activate = function(params) {
            var d = $.Deferred();

            strategy.strategyVM.getStep();

            d.resolve();
            return d.promise();
        };

    };

    return Component;

});

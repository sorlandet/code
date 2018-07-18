// An example configuration file.
exports.config = {
    // The address of a running selenium server.
    // seleniumAddress: 'http://localhost:4444/wd/hub',
    // Make use you check the version in the folder
    //seleniumServerJar: '../selenium/selenium-server-standalone-2.44.0.jar',

    // Capabilities to be passed to the webdriver instance.
    capabilities: {
        browserName: 'firefox'
    },
    // Spec patterns are relative to the current working directly when
    // protractor is called.
    //comment as we use gulp-protractor
    //specs: ['test/e2e/**/*-spec.js'],
    onPrepare: function() {
        var jasmineReporters = require('jasmine-reporters');
        jasmine.getEnv().addReporter(new
            jasmineReporters.JUnitXmlReporter({
                savePath: '../var/tests-spa-js/',
                consolidateAll: true,
                filePrefix: 'firefox'
            })
        );

        var AllureReporter = require('./e2e/reporters/jasmine2-allure-reporter');
        jasmine.getEnv().addReporter(new AllureReporter({
            resultsDir: '../var/tests-spa-js/allure-results'
        }));
        jasmine.getEnv().afterEach(function(done) {
            browser.takeScreenshot().then(function (png) {
                allure.createAttachment('Screenshot', function () {
                    return new Buffer(png, 'base64')
                }, 'image/png')();
                done();
            });
        });
    },
    params:{
        test: 'firefox'
    },
    // Options to be passed to Jasmine-node.
    jasmineNodeOpts: {
        showColors: true,
        defaultTimeoutInterval: 30000
    }
};

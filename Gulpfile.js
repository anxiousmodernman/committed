var gulp = require('gulp');
var browserify = require('browserify');
var source = require('vinyl-source-stream');
var del = require('del');

var paths = {
    jsSources: './static/js/**/*.js',  // any JS file in a subdir of /static/js
    buildDir: './static/public/js/',
    mainApp: './static/js/app.js',
    publicDir: './static/public'
};

gulp.task('build', ['clean'], function () {
    return browserify(paths.mainApp)
        .bundle()
        .pipe(source('bundled.js'))  // Only one bundled file for now, but we might end up w/ multiple
        .pipe(gulp.dest(paths.buildDir));
});

gulp.task('watch', function () {
    gulp.watch(paths.jsSources, ['build'])
});

gulp.task('clean', function () {
    console.log('Delete contents of ', paths.publicDir);
    del(paths.publicDir)
});

// runs when gulp is executed with no args
gulp.task('default', ['watch']);

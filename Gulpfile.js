var gulp = require('gulp');
// requires browserify and vinyl-source-stream
var browserify = require('browserify');
var source = require('vinyl-source-stream');


gulp.task('build', function() {
    return browserify('./static/js/app.js')
        .bundle()
        .pipe(source('bundled.js'))
        .pipe(gulp.dest('./static/public/js/'));
});


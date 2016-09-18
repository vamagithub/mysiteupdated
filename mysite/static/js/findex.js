(function($) {
    'use strict';
    
    $(function() {
        $('.js-file-input').each(function() {
            var $thisInput = $(this),
                $inputDisplay = $thisInput.siblings('.js-file-input-display');

            $thisInput.off('change.fileInput');

            if(!$inputDisplay.length) return;

            var inputOriginalText = $inputDisplay.text();

            $thisInput.on('change.fileInput', function() {
                var fileName;

                // If browser supports File API
                if(this.files) {
                    if(this.files.length) {
                        fileName = Array.prototype.slice.call(this.files, 0)
                            .map(function(fileObj) {
                                return fileObj.name;
                            }).
                            join(', ');
                    }
                } else {
                    var val = $(this).val();

                    if(val) {
                        var splitVal = val.split('\\');
                        fileName = splitVal[splitVal.length-1];
                    }
                }

                if(fileName) {
                    $inputDisplay.text(fileName);
                } else {
                    $inputDisplay.text(inputOriginalText);
                }
            });
        });
    });
})(jQuery);
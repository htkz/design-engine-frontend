addInstance = function(elementId) {
    // console.log(elementId);
    let pos = {x:1200, y:800};
    let color = elementInformation[elementId].color;
    let shortName = elementInformation[elementId].shortName;
    let nodeId = createInstance(pos, color, shortName);
    nodeInformation[nodeId] = elementInformation[elementId];
}

// Add element type to left menu
var elements = JSON.parse($('#elements').val());
for (var i = 0; i < elements.length; i++) {
    let element = elements[i];
    let elementId = element.pk;
    let info = element.fields;
    let name = info.name;
    // transfer null to ''(empty string)
    for (var j in info) {
        if(info[j] === null) {
            info[j] = '';
        }
    }
    elementInformation[elementId] = info;
    addElementChild(name, elementId);
    elementPool.push(elementId);
}


// Add dataStructure to left menu
var structures = JSON.parse($('#dataStructures').val());
for (var i = 0; i < structures.length; i++) {
    let structure = structures[i];
    let structureId = structure.pk;
    let info = structure.fields.value;
    dataStructures[structureId] = JSON.parse(info.replace(/'/g, "\"").replace(/None/g, '\"\"'));
    dataStructureNames.push(structureId);
    addDataStructureChild(structureId);
}

// add selected for top navbar
$('#navbarNav1').find('li').each(function(index, el) {
    $(el).click(function(event) {
        $(el).siblings().removeClass('selected');
        $(el).addClass('selected')
    });
});

$('#explore').click(function(event) {
    if(!curDataStructure) {
        swal({
          title: "No datastructer selected!",
          text: "Please select a datastructer first!",
          type: "error",
          timer: 1500,
          showConfirmButton: false,
        });
        $(this).siblings('#design').addClass('selected');
        $(this).removeClass('selected')
    } else {
        function_disable = true;
        showRadarTree();
    }

});

$('#design').click(function(event) {
    function_disable = false;
    hideRadarTree();
});


if($('#db-manage').val() === 'False') {
    // hide “Clear”, “Save Data Structure” buttons
    $('#clear').hide();
    $('#saveDataStructure').hide();
    // remove delete icon
    $('.fa-times-circle-o').each(function(index, el) {
        $(el).remove();
    });
    // resize width
    $('#leftSidenav').css('width', '240px');
    // delete elment-add button
    $('#panel-el').hide();
    // hide color and shortName
    $('#fieldset-color').hide();
    $('#fieldset-shortname').hide();
}

if(!menuVisibility) {
    $('#navbarNav1').css('visibility', 'hidden');
}

// popup struct info
swal({
  title: "Welcome",
  text: "Choose a data structure on the left side menu, to see its specification visually in the center of the screen.\
  Then click on each element in the visual specification to see its complete textual specification on the right side.",
  type: "success",
  showConfirmButton: true,
});

$('.quit').click(function(event) {
    $('.rightNav').animate({width: 0}, 400, 'linear')
});

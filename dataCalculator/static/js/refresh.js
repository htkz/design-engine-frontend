clearObject = function(obj) {
    for (var prop in obj) { if (obj.hasOwnProperty(prop)) { delete obj[prop]; } }
}

emptyBrowser = function() {
    graph.clear();
    clearObject(nameToId);
    clearObject(idToName);
    clearObject(id_to_pyid);
    clearObject(pyid_to_id);
    clearObject(nodeInformation);
    // clearObject(workLoadInformation);
    clearObject(modules);
    clearObject(moduleStructure);
    nodeStructure.length = 0;
    idPool.length = 0;
    // createNewWorkload();
    // changeSettingFormat();
}

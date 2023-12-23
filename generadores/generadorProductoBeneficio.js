// #################### Arreglos con IDs de beneficio ####################
benCabana = [36]
benBimini = [38]
benTent = [39]
benSillas = [37]
benDiamond = [3, 10, 11, 12, 13, 14, 15, 16, 25, 26]
benPlatino = [3, 4, 5, 6, 7, 8, 9, 27, 28]
benGold = [3, 29, 30, 34,35]
benPlanAlimentosUnDia = [24,17,19,41]
benUnaComida = [22,17,19]
benDosComidas = [23,17,18,19]
benFlash = [31]
benEstacionamiento = [32]
benFoodGarden = [40]
benBoletoUnDia = [1]
benBoletoUnDiaHurr= [2]
benVIPex = [42,43,44]
benVIPtour = [45,58,47,49,52,51,53,54,56,57]
benTourHurricane = [45,46,47,48,50,53,54,55]
benVIPxmas = [58,59,60,61,62]
benVIPkids = [63,59,60,61,62]



// #################### Arreglos con los plu ####################
pluCabana = [10078449, 10096638, 10107711, 10093930, 10107712, 10107714, 10118600, 10119152, 10120570, 10120571]
pluBimini = [10078450, 10107715, 10107716, 10093523, 10107717, 10114209, 10114211, 10114213, 10120575, 10120576]
pluTent = [10093994, 10093522, 10093998, 10109599, 10114229, 10114228, 10118594, 10118595, 10118596, 10118597, 10120591, 10120592]
pluSillas = [10096631, 10096632, 10114197, 10120572, 10120573, 10120574]
pluDiamond = [10105271, 10120621, 10123094, 10105272, 80004527, 10098203, 80004531, 10117397, 10098207, 10104105, 10120620, 10123097, 10117469, 10105268, 10098208, 80004543, 80004547]
pluPlatino = [10105273, 10098200, 10120579, 10123095, 10105263, 10098201, 10117384, 10100798, 10117989, 10119969, 10098204, 10104102, 10105270, 10120581, 10123098, 10105267, 10117445, 80004539, 10098205, 10118207, 10119977, 10119975, 10114506]
pluGold = [10123096, 80004519, 10098752, 10118026, 10118248, 10123099, 10100054, 80004535, 10100058, 10098754]
pluPlanAlimentosUnDia = [10104581, 10104580, 10104600, 10104617]
pluUnaComida =[10116980, 10116982, 10104080, 10111736, 10100217, 10100772, 10116981, 10116986, 10116988, 10116987, 10116989, 10116991, 10100218, 10116515, 10116517, 10100774, 10104584, 10116516, 10116521, 10100169, 10100718, 10116522, 10116524, 10116526, 10100170, 10100719, 10116518, 10116519, 10116520]
pluDosComidas= [10116996, 10116997, 10116998, 10117002, 10117004, 10099346, 10098979, 10111737, 10100773, 10117003, 10104076, 10099349, 10117005, 10117008, 10100216, 10116533, 10116535, 10116540, 10098068, 10098974, 10099286, 10099290, 10104583, 10099289, 10116534, 10100775, 10116541, 10116543, 10100720, 10116545, 10100721, 10100168, 10116536, 10116537, 10116539]
pluFlash = [10123274, 10114507]
pluEstacionamiento = [10075795]
pluFood = [10120593]
pluBoletoUnDia = [10088751, 10088375, 10095987, 10095985, 10117734, 10117733, 10091426, 10115154, 90001457]
pluBoletoUnDiaHurr = [10081280, 10091425, 90001430, 10105274, 10082147, 10088370, 10088373, 10088374]
pluVIPex = [10091705, 10098325, 10098326, 10098323, 10112783]
pluVIPtour = [10102070]
pluTourHurricane = [10096432]
pluVIPxmas = [10091704, 10098324, 10048482]
pluVIPkids = [10123466, 10100694, 10123467, 10123465, 10100695]

// #################### PARA ESCRIBIR EL ARCHIVO SQL ####################
const fs = require('fs');

function registrosPorGrupo(plu, ben) {
    let registrosGrupales = '';
    for (let i = 0; i < plu.length; i++) {
        for (let j = 0; j < ben.length; j++) {
            registrosGrupales += `\t, (${plu[i]}, ${ben[j]})\n`
        }
    }
    return registrosGrupales;
}

//contenido del archivo, insert

const insertContent = "I NSERT INTO  producto_beneficio(\n\tplu\n\t, beneficio_id \n)\nVALUES\n";
let registros = '';

registros = registrosPorGrupo(pluCabana, benCabana)
            + registrosPorGrupo(pluBimini, benBimini)
            + registrosPorGrupo(pluTent, benTent)
            + registrosPorGrupo(pluSillas, benSillas)
            + registrosPorGrupo(pluDiamond, benDiamond)
            + registrosPorGrupo(pluPlatino, benPlatino)
            + registrosPorGrupo(pluGold, benGold)
            + registrosPorGrupo(pluPlanAlimentosUnDia, benPlanAlimentosUnDia)
            + registrosPorGrupo(pluUnaComida, benUnaComida)
            + registrosPorGrupo(pluDosComidas, benDosComidas)
            + registrosPorGrupo(pluFlash, benFlash)
            + registrosPorGrupo(pluEstacionamiento, benEstacionamiento)
            + registrosPorGrupo(pluFood, benFoodGarden)
            + registrosPorGrupo(pluBoletoUnDia, benBoletoUnDia)
            + registrosPorGrupo(pluBoletoUnDiaHurr, benBoletoUnDiaHurr)
            + registrosPorGrupo(pluVIPex, benVIPex)
            + registrosPorGrupo(pluVIPtour, benVIPtour)
            + registrosPorGrupo(pluTourHurricane, benTourHurricane)
            + registrosPorGrupo(pluVIPxmas, benVIPxmas)
            + registrosPorGrupo(pluVIPkids, benVIPkids)

let contenidoCompelto = `${insertContent}  ${registros};`;

fs.writeFile('producto_beneficio.sql', contenidoCompelto, err => {
    if (err) {
        console.err;
        return;
    }
})
import authorities from "./qlacref_authorities/records.json";


const laReducer = (map, value) => {
    map[value.la_id] = value;
    return map;
  };
  
export const laMap = authorities.map((x) => {
    return {
    la_id: x.UTLA21CD,
    la_name: x.UTLA21NM,
    };
}).reduce(laReducer, {});

export const laData = Object.values(laMap).sort((a, b) =>
    a.la_name > b.la_name ? 1 : -1
);

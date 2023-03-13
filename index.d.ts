declare module 'quality-lac-data-ref-authorities';

export type LaData = {
    la_id: string;
    la_name: string;
};

export type LaMap = {
    [key: string]: LaData;
};

export const laMap: LaMap;
export const laData: [LaData];

export declare class Logger {
    static instances: {
        [key: string]: Logger;
    };
    private readonly id;
    private readonly start;
    constructor(id: string);
    debug(...args: any): void;
    getTime(): number;
    static create(id: string): void;
    static destroy(id: string): void;
    static getInstance(id: string): Logger;
    info(...args: any): void;
    error(...args: any): void;
}

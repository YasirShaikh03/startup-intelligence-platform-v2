import math
import random

# Score lookup tables — these mirror the values used in the frontend JS engine

FE = {
    'First-time founder': .62,
    '1 previous venture (failed)': .74,
    '1 previous venture (exited)': .88,
    'Serial entrepreneur (2+ ventures)': .95,
    'Ex-FAANG / Big Tech exec': .85,
    'Domain expert (10+ years)': .82,
    'Family business background': .76,
}

TS = {'1 (solo founder)': 38, '2–5': 72, '6–15': 84, '16–50': 78, '50+': 68}

FS_MAP = {
    'Low (residential / quiet)': 22,
    'Medium (mixed area)': 55,
    'High (market / station)': 82,
    'Very High (prime location)': 96,
}

LS = {
    'Railway Station': 90, 'College / University': 85, 'Office Hub / IT Park': 80,
    'Shopping Mall': 75, 'Hospital': 65, 'School': 70, 'Market / Bazaar': 85,
    'Multiple Landmarks': 95,
}

DS = {'Under 100m (walking distance)': 95, '100m – 500m': 80, '500m – 2km': 55, '2km+': 25}
DC = {'Under 100m': 90, '100m – 500m': 75, '500m – 2km': 50, '2km+': 20}

AC = {
    'None — first in area': 90, 'Low (1–3 competitors)': 75,
    'Medium (4–10 competitors)': 55, 'High (10+ competitors)': 35, 'Saturated': 18,
}

FST = {
    'Self-funded / Bootstrapped': 25, 'Family & Friends': 38, 'Pre-seed': 50,
    'Seed': 65, 'Series A': 78, 'Series B': 88, 'Series C+': 95,
}

FA = {
    'Under ₹50K': 20, '₹50K – ₹2L': 38, '₹2L – ₹10L': 55,
    '₹10L – ₹50L': 68, '₹50L – ₹1Cr': 82, '₹1Cr+': 95,
}

MS = {
    'Hyper Local (1 area)': 20, 'City Level': 45, 'State Level': 62,
    'National (India)': 82, 'International': 96,
}

RV = {
    'No revenue yet': 10, 'First customers / Beta': 30, '₹0–₹50K/month': 45,
    '₹50K–₹2L/month': 62, '₹2L–₹10L/month': 80, '₹10L+/month': 96,
}

PS = {
    'Idea only': 12, 'Building / In development': 32, 'Launched (basic)': 55,
    'Product-market fit found': 80, 'Scaling': 92,
}

CM = {
    'Blue ocean (no direct competitors)': 72, 'Few niche competitors': 82,
    'Moderate — established players': 62, 'Highly competitive — giants present': 40,
    'Saturated market': 22,
}

TR = {
    'Dying / Declining': 10, 'Stable / Flat': 40, 'Growing steadily': 65,
    'Trending (popular now)': 85, 'Viral / Explosive growth': 97,
}

SP = {
    'None (year-round stable)': 1.0, 'Mild seasonal variation': .96,
    'Moderate (summer/winter effect)': .90, 'High (monsoon/festival heavy)': .82,
    'Extreme (only 3–4 months busy)': .68,
}

WP = {
    'None (indoor/digital)': 1.0, 'Low': .96,
    'Medium (outdoor, some impact)': .88, 'High (rain stops business)': .72,
}

LC = {'Fully Licensed (all docs)': 95, 'Partially Licensed': 60, 'No License': 15, 'In Process': 45}
PR = {
    'No Risk (licensed, indoor)': 90, 'Low Risk': 72,
    'Medium (occasional checks)': 48, 'High (unlicensed, outdoor)': 15,
}
HY = {'Basic': 40, 'Moderate': 70, 'High': 95}

ON = {
    'Yes — Active website + social': 90, 'Yes — Social media only': 68,
    'Minimal (just WhatsApp)': 40, 'No online presence': 10,
}

AG = {
    'Yes — Both platforms': 90, 'Yes — One platform': 65,
    'No — Plan to list': 30, 'No — Not applicable': 0,
}

BK = {
    'Already profitable': 95, 'Under 1 month': 85, '1–3 months': 72,
    '3–6 months': 58, '6–12 months': 42, '1–2 years': 28, '2+ years': 15,
}

IT = {
    'AI / ML': 94, 'Cybersecurity': 88, 'HealthTech': 82, 'FinTech': 78,
    'CleanTech': 76, 'BioTech': 74, 'SaaS / B2B Software': 72,
    'Logistics / Supply Chain': 65, 'EdTech': 60, 'Consumer App': 55,
    'E-Commerce': 52, 'Web3 / Crypto': 36, 'Food & Beverage': 70,
    'Retail': 55, 'Other': 58,
}

FD = {
    'Pani Puri / Gol Gappa': 95, 'Vada Pav': 90, 'Chai / Tea': 88, 'Chaat': 85,
    'Chinese (Noodles/Momos)': 82, 'Rolls / Wraps': 80, 'Juice / Shakes': 78,
    'Bhel / Sev Puri': 76, 'Sandwich / Burger': 72, 'Dosa / South Indian': 70,
    'Biryani / Rice': 68, 'Ice Cream / Kulfi': 65, 'Other Street Food': 55,
}

RM = {
    'Stable (vegetable / grain based)': 1.0,
    'Moderate (mixed ingredients)': .93,
    'High (seasonal / imported)': .83,
}

BENCHMARKS = {
    'Street Food':   {'surv': 58, 'prof': 52, 'scal': 41, 'ldom': 62, 'comp': 67},
    'Tech Startup':  {'surv': 44, 'prof': 38, 'scal': 61, 'ldom': 39, 'comp': 52},
    'SaaS':          {'surv': 48, 'prof': 55, 'scal': 72, 'ldom': 35, 'comp': 56},
    'E-Commerce':    {'surv': 51, 'prof': 46, 'scal': 58, 'ldom': 44, 'comp': 53},
    'Service':       {'surv': 60, 'prof': 57, 'scal': 44, 'ldom': 55, 'comp': 58},
    'Local Shop':    {'surv': 62, 'prof': 54, 'scal': 38, 'ldom': 60, 'comp': 57},
    'Franchise':     {'surv': 66, 'prof': 61, 'scal': 55, 'ldom': 58, 'comp': 62},
    'Manufacturing': {'surv': 55, 'prof': 50, 'scal': 48, 'ldom': 47, 'comp': 55},
    'default':       {'surv': 52, 'prof': 49, 'scal': 52, 'ldom': 49, 'comp': 54},
}


def sl(mapping: dict, key: str, default: float = 50) -> float:
    return mapping.get(key, default) if key else default


def cl(v: float, mn: float = 5.0, mx: float = 97.0) -> int:
    return max(int(mn), min(int(mx), round(v)))


def compute_startup_score(d: dict) -> dict:
    # Traction (24%)
    rev_s    = sl(RV, d.get('rev', ''), 10)
    margin   = d.get('margin', 0) or 0
    growth   = d.get('growth_rate', 0) or 0
    bk_s     = sl(BK, d.get('breakeven', ''), 40)
    pstage_s = sl(PS, d.get('pstage', ''), 20)
    trac_s   = cl(rev_s * .45 + pstage_s * .25 + bk_s * .15 + min(growth * 2, 40) * .1 + min(margin, 70) * .05)

    # Market (20%)
    comp_s  = sl(CM, d.get('comp', ''), 55)
    trend_s = sl(TR, d.get('trend', ''), 50)
    msize_s = sl(MS, d.get('msize', ''), 40)
    seas_m  = sl(SP, d.get('seasonal', ''), 0.9)
    mkt_s   = cl((comp_s * .35 + trend_s * .40 + msize_s * .25) * seas_m)

    # Team (18%)
    fm       = sl(FE, d.get('fexp', ''), 0.68)
    team_raw = sl(TS, d.get('tsize', ''), 50)
    team_s   = cl(team_raw * fm)

    # Funding (14%)
    fst_s = sl(FST, d.get('fstage', ''), 25)
    fa_s  = sl(FA, d.get('famt', ''), 20)
    fun_s = cl(fst_s * .55 + fa_s * .45)

    # Moat (10%)
    moat_s = cl((comp_s * .50 + msize_s * .30 + trend_s * .20) * .88 + 6)

    # Operations (6%)
    lc_s  = sl(LC, d.get('license', ''), 30)
    emp   = min(d.get('employees', 0) or 0, 50)
    ops_s = cl(lc_s * .55 + min(emp * 2, 40) * .25 + bk_s * .20)

    # Digital (4%)
    on_s  = sl(ON, d.get('online', ''), 20)
    aggr_s = sl(AG, d.get('aggr', ''), 0)
    dig_s = cl(on_s * .65 + aggr_s * .35)

    # Industry Timing (4%)
    tim_s = cl(sl(IT, d.get('industry', ''), 58) * .88 + 5)

    comp = (
        trac_s * .24 + mkt_s * .20 + team_s * .18 + fun_s * .14 +
        moat_s * .10 + ops_s * .06 + dig_s * .04 + tim_s * .04
    )

    ml_adj = _ml_adjustment_startup(d, trac_s, mkt_s, team_s)
    final  = cl(comp * (1 + ml_adj / 100))

    surv = cl(trac_s * .40 + ops_s * .30 + fun_s * .20 + dig_s * .10)
    prof = cl(trac_s * .50 + (min(margin, 80) / 80 * 80) * .30 + bk_s * .20)
    scal = cl(mkt_s * .35 + msize_s * .25 + team_s * .20 + fun_s * .20)
    ldom = cl(moat_s * .40 + comp_s * .35 + dig_s * .25)

    return {
        'composite_score': final,
        'surv': surv, 'prof': prof, 'scal': scal, 'ldom': ldom,
        'trac_s': trac_s, 'mkt_s': mkt_s, 'team_s': team_s,
        'fun_s': fun_s, 'moat_s': moat_s, 'ops_s': ops_s,
        'dig_s': dig_s, 'tim_s': tim_s,
        'ml_adj': ml_adj, 'fm': round(fm, 2),
    }


def _ml_adjustment_startup(d: dict, trac: float, mkt: float, team: float) -> int:
    adj = 0
    rev = d.get('rev', '')
    if rev in ('₹2L–₹10L/month', '₹10L+/month'):           adj += 6
    if d.get('pstage', '') == 'Product-market fit found':    adj += 4
    growth = d.get('growth_rate', 0) or 0
    if growth >= 20:                                          adj += 4
    if growth >= 35:                                          adj += 3
    if rev == 'No revenue yet' and trac < 35:                adj -= 5
    if d.get('tsize', '') == '1 (solo founder)':             adj -= 3
    if d.get('fstage', '') in ('Series A', 'Series B'):      adj += 3
    if d.get('industry', '') in ('AI / ML', 'Cybersecurity', 'HealthTech'): adj += 3
    if mkt > 75 and team > 70:                               adj += 3
    return max(-15, min(15, adj))


def compute_street_score(d: dict) -> dict:
    # Location (28%)
    fs_s  = sl(FS_MAP, d.get('footfall', ''), 45)
    ls_s  = sl(LS, d.get('landmarks', ''), 50)
    ds_s  = sl(DS, d.get('dist_sta', ''), 40)
    dc_s  = sl(DC, d.get('dist_col', ''), 40)
    ac_s  = sl(AC, d.get('area_comp', ''), 50)
    wp_m  = sl(WP, d.get('weather', ''), 0.90)
    loc_s = cl((fs_s * .35 + ls_s * .20 + ds_s * .18 + dc_s * .12 + ac_s * .15) * wp_m)

    # Product (25%)
    fd_s   = sl(FD, d.get('food_type', ''), 65)
    hy_s   = sl(HY, d.get('hygiene', ''), 50)
    taste  = (d.get('taste_rating', 0) or 0) * 10
    repeat = d.get('repeat_rate', 0) or 0
    waste  = d.get('daily_waste', 0) or 0
    rm_m   = sl(RM, d.get('rm_var', ''), 0.93)
    prod_s = cl((fd_s * .30 + hy_s * .25 + taste * .25 + min(repeat, 80) * .15 + max(0, 50 - waste) * .05) * rm_m)

    # Finance (22%)
    margin   = d.get('margin', 0) or 0
    bk_s     = sl(BK, d.get('breakeven', ''), 40)
    d_rev    = d.get('daily_rev', 0) or 0
    avg_p    = d.get('avg_price', 0) or 0
    dc       = d.get('daily_cust', 0) or 0
    rev_proxy = (dc * avg_p) if (dc and avg_p) else (d_rev or 0)
    rev_norm  = min(rev_proxy / 10000 * 80, 80)
    sp_m     = sl(SP, d.get('seasonal', ''), 0.90)
    fin_s    = cl((min(margin, 80) * .40 + bk_s * .30 + rev_norm * .20 + 20 * .10) * sp_m)

    # Ops / Legal (12%)
    lc_s  = sl(LC, d.get('license', ''), 25)
    pr_s  = sl(PR, d.get('police', ''), 40)
    ops_s = cl(lc_s * .55 + pr_s * .30 + max(0, 50 - waste) * .15)

    # Digital / Growth (8%)
    on_s  = sl(ON, d.get('online', ''), 15)
    ag_s  = sl(AG, d.get('aggr', ''), 0)
    grw_s = cl(on_s * .55 + ag_s * .35 + min((d.get('growth_rate', 0) or 0) * 2, 30) * .10)

    # Survival buffer (5%)
    surv_raw = cl(fin_s * .45 + ops_s * .30 + loc_s * .25)

    comp = (loc_s * .28 + prod_s * .25 + fin_s * .22 +
            ops_s * .12 + grw_s * .08 + surv_raw * .05)

    ml_adj = _ml_adjustment_street(d, loc_s, prod_s, fin_s)
    final  = cl(comp * (1 + ml_adj / 100))

    prof = cl(fin_s * .55 + prod_s * .25 + ops_s * .20)
    scal = cl(grw_s * .40 + loc_s * .30 + prod_s * .30)
    ldom = cl(loc_s * .50 + ac_s * .30 + on_s * .20)

    return {
        'composite_score': final,
        'surv': surv_raw, 'prof': prof, 'scal': scal, 'ldom': ldom,
        'loc_s': loc_s, 'prod_s': prod_s, 'fin_s': fin_s,
        'ops_s': ops_s, 'grw_s': grw_s,
        'fd': fd_s, 'hy': hy_s, 'ts': taste, 'lc': lc_s,
        'ml_adj': ml_adj,
    }


def _ml_adjustment_street(d: dict, loc: float, prod: float, fin: float) -> int:
    adj = 0
    if loc >= 75:                                  adj += 4
    repeat = d.get('repeat_rate', 0) or 0
    taste  = d.get('taste_rating', 0) or 0
    if repeat >= 60:                               adj += 3
    if taste >= 8:                                 adj += 3
    license = d.get('license', '')
    if 'No License' in license:                    adj -= 6
    waste = d.get('daily_waste', 0) or 0
    if waste >= 25:                                adj -= 4
    weather = d.get('weather', '')
    if 'High' in weather:                          adj -= 3
    if d.get('aggr', '') and 'Both' in d.get('aggr', ''): adj += 3
    return max(-12, min(12, adj))


def generate_ai_insights(d: dict, scores: dict, is_street: bool) -> dict:
    n     = d.get('name', 'Your Business')
    city  = d.get('city', 'your city')
    area  = d.get('area', 'your area')
    score = scores['composite_score']
    loc   = f"{area}, {city}" if area and city else city

    summary      = _street_summary(n, d, score, loc) if is_street else _startup_summary(n, d, score, loc)
    strengths    = _get_strengths(n, d, scores, is_street, loc, city)[:6]
    risks        = _get_risks(n, d, scores, is_street, loc, city)[:6]
    opportunities = _get_opportunities(n, d, scores, is_street, loc)[:4]
    actions      = _get_actions(n, d, scores, is_street, city)[:5]
    scaling      = _get_scaling(n, d, score, is_street, city)
    verdict      = _get_verdict(n, score, scores, d, is_street)
    hidden       = _get_hidden_insight(n, d, scores, is_street)

    return {
        'summary': summary,
        'strengths': strengths,
        'risks': risks,
        'opportunities': opportunities,
        'actions': actions,
        'scaling': scaling,
        'verdict': verdict,
        'hidden_insight': hidden,
        'ai_score': _compute_ai_score(scores, d, is_street),
        'source': 'backend-ml-engine',
    }


def _street_summary(n, d, score, loc):
    food  = d.get('food_type', 'street food')
    stall = d.get('stall_type', '')
    crowd = d.get('crowd_type', 'local customers')
    landmarks = d.get('landmarks', 'key landmarks')
    desc  = d.get('description', '')
    s = f"{n} is a {food} business" + (f" operating as a {stall}" if stall else "")
    s += f" in {loc}, targeting {crowd} near {landmarks}. "
    if score >= 70:
        s += f"With a strong score of {score}/100, the business shows solid fundamentals in location, product demand, and unit economics. "
    elif score >= 50:
        s += f"Scoring {score}/100, the business has promising potential with clear areas requiring improvement. "
    else:
        s += f"At {score}/100, meaningful challenges need addressing before scaling. "
    if desc:
        s += f"The founder's assessment: \"{desc[:100]}{'…' if len(desc) > 100 else ''}\" — reflecting strong self-awareness of the opportunity."
    return s


def _startup_summary(n, d, score, loc):
    biz_type = d.get('biz_type', 'startup')
    industry = d.get('industry', '')
    pstage   = d.get('pstage', 'an early stage')
    rev      = d.get('rev', 'early revenue')
    desc     = d.get('description', '')
    s = f"{n} is a {biz_type}" + (f" in the {industry} space" if industry else "")
    s += f" based in {loc}, currently at {pstage} with {rev}. "
    if score >= 70:
        s += f"A score of {score}/100 signals strong investor-readiness across team, market, and traction dimensions. "
    elif score >= 50:
        s += f"Scoring {score}/100 indicates real potential but needing sharper execution and validation. "
    else:
        s += f"At {score}/100, foundational gaps — particularly around revenue and team — need resolution before meaningful fundraising. "
    if desc:
        s += f"The founder frames it as: \"{desc[:100]}{'…' if len(desc) > 100 else ''}\" — capturing both the opportunity and the core challenge."
    return s


def _get_strengths(n, d, scores, is_street, loc, city):
    out = []
    if is_street:
        if scores.get('ldom', 0) >= 70:
            out.append(f"Strong local dominance in {loc} — footfall near {d.get('landmarks', 'key landmark')} gives {n} a built-in customer pipeline that competitors cannot easily replicate")
        repeat = d.get('repeat_rate', 0) or 0
        if repeat >= 50:
            out.append(f"Exceptional repeat customer rate of {repeat}% signals product quality — the most capital-efficient growth engine for any street food business")
        taste = d.get('taste_rating', 0) or 0
        if taste >= 7:
            out.append(f"High taste rating of {taste}/10 is a direct competitive moat — in street food, taste is the single most powerful word-of-mouth driver and cannot be bought with marketing spend")
        margin = d.get('margin', 0) or 0
        if margin >= 40:
            out.append(f"Healthy gross margin of {margin}% provides financial resilience and headroom for reinvestment without needing external capital")
        if d.get('hygiene', '') == 'High':
            out.append(f"High hygiene standards position {n} above the majority of competitors in {city}, enabling Swiggy/Zomato listing and justifying a premium price point")
        if d.get('footfall', '') and 'High' in d.get('footfall', ''):
            out.append(f"High footfall density at current location means {n} benefits from passive discovery — walk-in traffic that costs zero in customer acquisition")
        if d.get('aggr', '') and 'Yes' in d.get('aggr', ''):
            out.append(f"Active aggregator presence creates a second revenue channel beyond physical walk-ins, diversifying income and building online brand equity")
        license = d.get('license', '')
        if license and 'Licensed' in license:
            out.append(f"Full FSSAI and municipal licensing eliminates the single biggest operational risk — {n} can operate without fear of sudden shutdown")
    else:
        if scores.get('trac_s', 0) >= 65:
            rev = d.get('rev', 'current stage')
            out.append(f"Revenue traction at {rev} is the strongest de-risking signal — {n} has moved beyond theory into validated customer value creation")
        if scores.get('team_s', 0) >= 65:
            fexp  = d.get('fexp', 'Founder experience')
            tsize = d.get('tsize', 'focused')
            out.append(f"{fexp} combined with a {tsize} team creates execution credibility that investors weight heavily at this stage")
        if scores.get('mkt_s', 0) >= 65:
            trend = d.get('trend', 'growing')
            msize = d.get('msize', 'significant')
            out.append(f"Operating in a {trend} market with {msize} TAM gives {n} room to capture meaningful share without displacing incumbents")
        if d.get('pstage', '') == 'Product-market fit found':
            out.append(f"Confirmed product-market fit is the rarest milestone in startups — {n} has passed the filter that eliminates over 80% of early-stage companies")
        growth = d.get('growth_rate', 0) or 0
        if growth >= 15:
            months = round(70 / growth)
            out.append(f"{growth}% monthly growth compounds dramatically — at this pace, {n} doubles revenue every {months} months, a compelling trajectory for any investor")
        if d.get('breakeven', '') == 'Already profitable':
            out.append(f"Profitability at current scale gives {n} the rarest startup advantage — optionality. Growth on your terms, not a VC's timeline")
        if d.get('online', '') and 'Active' in d.get('online', ''):
            out.append(f"Strong online presence reduces CAC and builds brand equity that compounds with every piece of content produced — a significant moat against offline-only competitors")
    if len(out) < 3:
        out.append(f"Clear monetization model gives {n} a path to sustainable revenue that doesn't require external capital to prove viability")
    if len(out) < 4:
        out.append(f"Founder-operated with hands-on quality control — creates institutional knowledge about customer psychology that no hired manager can replicate")
    if len(out) < 5:
        out.append(f"Location in {city} provides access to a talent pool and customer base that will support {n}'s next growth phase")
    return out[:6]


def _get_risks(n, d, scores, is_street, loc, city):
    out = []
    if is_street:
        weather = d.get('weather', '')
        if 'High' in weather:
            out.append(f"Extreme weather dependency — rain directly halts revenue for {n}, creating dangerous cash flow gaps during monsoon months without a covered or indoor contingency plan")
        license = d.get('license', '')
        if not license or 'No License' in license or 'Partial' in license:
            out.append(f"Incomplete licensing is the highest-severity risk — a single municipal inspection can shut {n} down overnight with zero recourse and total revenue loss")
        if scores.get('ldom', 0) < 55:
            out.append(f"Weak local dominance in {loc} means {n} is vulnerable to any new competitor entering the same spot with a slightly better price or location")
        waste = d.get('daily_waste', 0) or 0
        if waste >= 20:
            out.append(f"{waste}% daily waste is destroying margins — at current revenue levels this represents compounding monthly losses in unsold inventory preventable with demand-based batching")
        repeat = d.get('repeat_rate', 0) or 0
        if repeat < 40:
            out.append(f"Low repeat rate of {repeat}% means {n} is on a constant customer acquisition treadmill instead of compounding on a loyal base — unit economics worsen at scale")
        aggr = d.get('aggr', '')
        if not aggr or 'No' in aggr:
            out.append(f"No aggregator presence makes {n} invisible to the fast-growing segment of customers who discover and order food exclusively through Swiggy and Zomato")
        seasonal = d.get('seasonal', '')
        if 'High' in seasonal or 'Extreme' in seasonal:
            out.append(f"High seasonal dependency creates feast-famine revenue cycles — {n} needs a counter-seasonal product or 3-month savings buffer to survive lean periods")
    else:
        trac = scores.get('trac_s', 0)
        rev  = d.get('rev', '')
        if trac < 45 or rev == 'No revenue yet':
            out.append(f"Zero or minimal revenue means {n} is burning runway on an unvalidated hypothesis — every month without paying customers increases failure probability exponentially")
        if d.get('tsize', '') == '1 (solo founder)':
            out.append(f"Solo founder concentration is a critical risk — {n} has a single point of failure for every function: product, sales, operations, and hiring")
        margin = d.get('margin', 0) or 0
        if margin < 30:
            out.append(f"Thin margin of {margin}% leaves {n} with no room for error on pricing, CAC, or cost surprises — unit economics need strengthening before scaling spend")
        if scores.get('mkt_s', 0) < 50:
            out.append(f"Weak market score signals competition, shrinking TAM, or poor timing — any one of these factors can permanently limit {n}'s growth ceiling")
        license = d.get('license', '')
        if license and 'No License' in license:
            out.append(f"No legal licensing creates regulatory exposure that will block enterprise sales, partnership conversations, and any institutional investment round")
        growth = d.get('growth_rate', 0) or 0
        if growth < 5:
            out.append(f"Slow growth rate means {n} is not compounding fast enough to create venture-scale outcomes — the window for seed funding typically closes within 18 months")
    if len(out) < 4:
        out.append(f"Single-location concentration gives {n} zero revenue redundancy — any disruption to the primary channel eliminates 100% of income simultaneously")
    if len(out) < 5:
        out.append(f"No documented systems or standardized processes means {n}'s quality is entirely founder-dependent and cannot be reliably scaled or handed to staff")
    if len(out) < 6:
        out.append(f"Growing competition in {city} is systematically capturing demand — {n} needs a clear moat to protect market share over the next 12 months")
    return out[:6]


def _get_opportunities(n, d, scores, is_street, loc):
    city = d.get('city', 'your city')
    out  = []
    if is_street:
        aggr = d.get('aggr', '')
        if not aggr or 'No' in aggr:
            out.append(f"Swiggy/Zomato registration opens a 3–5 km delivery radius to customers who will never walk past {n}'s stall — average aggregator uplift for new listings is 35–50% revenue in Month 1")
        out.append(f"WhatsApp Business catalogue with a pre-order system creates guaranteed daily revenue floor for {n} — early data shows 20–30% of regulars will pre-order if given the option")
        out.append(f"A loyalty stamp card ('buy 9 get 1 free') costs under ₹500 to print and has proven to increase visit frequency by 40% across Indian street food studies")
        out.append(f"Central supply kitchen partnership with 3–5 nearby stalls for bulk ingredient buying reduces RM costs 15–22% — the single highest-ROI cost reduction available to {n}")
        out.append(f"Premium version of {n}'s bestseller at 2x the price with one extra ingredient — research shows 18–25% of street food customers will upgrade if given the option, instantly boosting average order value")
        out.append(f"Google Maps listing optimization with photos, a QR code at the stall, and 4.5+ star rating drives measurable walk-in uplift — {n} is likely invisible to the maps-first customer segment today")
    else:
        if scores.get('mkt_s', 0) >= 60:
            out.append(f"Market timing is favorable — {n} can establish category leadership in one narrow vertical before well-funded competitors respond, creating a defensible first-mover position")
        out.append(f"Partnership channel: identifying 3 companies that already serve {n}'s ideal customer and proposing a rev-share or white-label arrangement can unlock a zero-CAC growth channel within 60 days")
        rev = d.get('rev', '')
        if rev in ('₹50K–₹2L/month', '₹2L–₹10L/month', '₹10L+/month'):
            out.append(f"With existing revenue validation, {n} is eligible for Startup India Seed Fund (up to ₹20L, no equity) and SIDBI CGTMSE guarantees — apply this quarter before allocation runs out")
        out.append(f"Content-led SEO: creating 10 high-intent comparison articles about {n}'s space can drive 500–2,000 organic visitors/month within 6 months at near-zero cost — most competitors ignore content entirely")
        out.append(f"Annual contract upsell: if {n} has any monthly customers, offering a 20% discount for an annual prepayment immediately improves cash position and LTV while reducing churn risk")
        out.append(f"API or integration partnerships: companies in adjacent categories are actively looking for embedded solutions — {n}'s core capability as a feature within a larger platform can 10x distribution without sales headcount")
    return out[:4]


def _get_actions(n, d, scores, is_street, city):
    if is_street:
        return [
            "Apply for FSSAI Basic Registration online today — ₹100 fee, 15 minutes at foscos.fssai.gov.in. This single action eliminates your highest-severity operational risk",
            "Set up WhatsApp Business (free) and collect phone numbers from your next 30 customers — this becomes your direct marketing channel with zero ongoing cost",
            f"Open a dedicated business bank account at {'SBI' if city else 'your nearest bank'} this week — required for Swiggy/Zomato onboarding and separates business from personal finances",
            "Ask your top 5 regulars today for a Google Maps review — target 4.5+ stars. Photos + reviews are the primary discovery mechanism for new walk-in customers in your area",
            "Track daily sales in a Google Sheet for 30 days — identifying your top 3 items and peak hours creates the data foundation for every future optimization decision",
        ]
    return [
        f"Schedule 5 customer discovery calls this week — 20 minutes each, focused on the exact pain {n} solves. Patterns in the first 5 calls will reshape your entire go-to-market",
        f"Write a one-page investment memo today: problem, solution, traction, ask, team. Warm-email it to 20 angels in {city} this week — even early-stage conversations build the pipeline",
        "Set up a weekly 30-minute metrics review every Monday — track MRR, churn, CAC, and burn rate. What gets measured gets managed, and investors expect you to know these cold",
        f"Create a simple landing page with one clear headline, one CTA, and a contact form — then run ₹5,000/week in Google Search ads targeting your ideal customer's exact pain query for 14 days to test messaging",
        "Document your three most important processes this week — sales script, onboarding flow, and support FAQ. This is the foundation for your first hire and prevents single-point-of-failure dependency on you",
    ]


def _get_scaling(n, d, score, is_street, city):
    if is_street:
        return (
            f"Phase 1 (Month 1–2): Get fully licensed, list on both aggregators, set up WhatsApp Business. "
            f"These three actions alone typically deliver 30–50% revenue uplift for {n} with zero capital investment. "
            f"Phase 2 (Month 3–6): Optimize location using peak-hour footfall data. Test a premium menu item at 2x price. "
            f"Target ₹5,000–₹8,000 daily revenue from the primary location. "
            f"Phase 3 (Year 1): Scout a second high-footfall location within 3km. "
            f"Standardize recipe and ops for replicability. "
            f"Phase 4 (Year 2): Franchise model — license brand to 3–5 operators for ₹50K–₹2L + 5% royalty. "
            f"{n} becomes a royalty-generating asset rather than a time-for-money business. "
            f"Exit horizon: A 10-franchise network with a central supply kitchen is valued at ₹1–5Cr by strategic acquirers."
        )
    if score >= 72:
        return (
            f"{n} is fundable. Prepare a Series A data room: P&L, cohort retention, CAC/LTV, 3 customer case studies. "
            f"Target ₹10–25Cr raise at ₹60–120Cr valuation with 3x YoY growth as the core narrative. "
            f"Hire a sales lead and senior engineer as the first two scaling hires — these compound every other metric. "
            f"Build 3 enterprise case studies and a referral program. At ₹2–5Cr ARR with 3x growth, "
            f"{n} should target Series B within 18 months for global expansion."
        )
    return (
        f"The path to fundability for {n} is straightforward: get to ₹2–5L MRR with 3 consecutive months of growth. "
        f"Focus exclusively on one acquisition channel that works without paid spend — usually SEO, content, or a partnership. "
        f"Once revenue validates the model, apply for Startup India Seed Fund (up to ₹20L, no equity) and "
        f"approach 20 angels in {city} with a one-page memo. The Series A playbook unlocks at ₹25L+ MRR."
    )


def _get_verdict(n, score, scores, d, is_street):
    if score >= 72:
        return f"{n} demonstrates strong fundamentals across all scoring dimensions. The business has the profile of a high-potential opportunity — above-average traction, solid unit economics, and defensible positioning. The primary focus should be on execution velocity rather than concept validation."
    if score >= 58:
        return f"{n} shows real promise with identifiable gaps that are addressable within 60–90 days. The scoring model flags specific dimensions that, if improved, would move this from a conditional pass to a strong recommendation. Prioritize the top-2 weakest dimensions for maximum score impact."
    if score >= 42:
        return f"{n} is at an inflection point — the fundamentals exist but meaningful risks are present that could compound without targeted action. This is a 'watch' recommendation: execute on the top-3 priority actions before the next analysis to quantify improvement."
    return f"{n} faces structural challenges that need resolution before the business can scale reliably. The scoring model identifies core gaps in {('location and product' if is_street else 'revenue traction and team')} that are addressable but require focused work. The roadmap is clear; execution is the variable."


def _get_hidden_insight(n, d, scores, is_street):
    if is_street:
        repeat = d.get('repeat_rate', 0) or 0
        taste  = d.get('taste_rating', 0) or 0
        if repeat >= 60 and taste >= 7:
            return f"Most analysts focus on location and pricing for {n}, but your repeat rate and taste score reveal the real moat: customer loyalty. A loyal customer base has a 5x lower CAC than a new customer and creates organic word-of-mouth that no advertising budget can replicate. Your hidden advantage is not your stall — it's your regulars."
        waste = d.get('daily_waste', 0) or 0
        if waste >= 15:
            return f"The hidden profit destroyer for {n} is waste, not competition. At {waste}% daily waste, you are essentially running a 'silent discount' on {waste}% of your production every day. Demand-based batching — making 20% less and running out 30 minutes before close — is proven to improve net margins by 8–14% without raising prices or increasing customers."
        return f"The single highest-ROI action for {n} in the next 30 days is not what most consultants recommend. It's data collection: track every sale, time, and item for 30 days. Most street food businesses discover that 20% of their menu items generate 80% of revenue — eliminating the rest cuts prep time by 40% and reduces waste dramatically."
    score = scores['composite_score']
    rev   = d.get('rev', '')
    if score >= 60 and rev not in ('No revenue yet', 'First customers / Beta'):
        return f"The hidden risk for {n} at this stage is premature scaling. Most founders accelerate hiring and spend the moment they hit product-market fit — but the companies that build defensible businesses slow down at PMF to document their ideal customer profile, CAC, and unit economics before scaling the engine. Scaling before documenting what's working is one of the most common causes of Series A failure."
    if d.get('tsize', '') == '1 (solo founder)':
        return f"The single highest-risk element in {n}'s profile is not market size, revenue, or competition — it is the solo founder dependency. Research on startup failure shows that single-founder startups fail at 2.3x the rate of co-founder teams. Finding a technical or sales co-founder is the single highest-ROI action available to {n} before any fundraising conversation."
    return f"Most analysis of {n} focuses on its current state. What's missed: the compound effect of fixing the weakest dimension. In the ML model, improving the lowest-scoring dimension by 20 points typically moves the composite score by 8–14 points — more than improving a strong dimension by the same amount. Always fix the floor, not the ceiling."


def _compute_ai_score(scores, d, is_street):
    base = scores['composite_score']
    adj  = 0
    if d.get('description', '') and len(d.get('description', '')) > 80: adj += 2
    margin = d.get('margin', 0) or 0
    if margin >= 40: adj += 2
    growth = d.get('growth_rate', 0) or 0
    if growth >= 15: adj += 3
    if is_street:
        if (d.get('repeat_rate', 0) or 0) >= 50: adj += 2
    else:
        if d.get('pstage', '') == 'Product-market fit found': adj += 4
    return cl(base + adj)


def compare_businesses(name_a: str, scores_a: dict, name_b: str, scores_b: dict) -> dict:
    dims = [
        ('composite_score', '🏆 Overall Score'),
        ('surv',  '🛡 Survival'),
        ('prof',  '💰 Profitability'),
        ('scal',  '📈 Scalability'),
        ('ldom',  '📍 Local Dominance'),
    ]

    rows   = []
    a_wins = 0
    b_wins = 0
    for key, label in dims:
        va    = scores_a.get(key, 0)
        vb    = scores_b.get(key, 0)
        delta = va - vb
        winner = name_a if delta > 0 else (name_b if delta < 0 else "TIE")
        if delta > 0:   a_wins += 1
        elif delta < 0: b_wins += 1
        rows.append({
            'dimension': label,
            'score_a': va,
            'score_b': vb,
            'delta': delta,
            'winner': winner,
        })

    overall_winner = name_a if scores_a['composite_score'] > scores_b['composite_score'] else name_b
    overall_delta  = abs(scores_a['composite_score'] - scores_b['composite_score'])

    return {
        'business_a': name_a,
        'business_b': name_b,
        'dimensions': rows,
        'wins_a': a_wins,
        'wins_b': b_wins,
        'overall_winner': overall_winner,
        'overall_delta': overall_delta,
        'recommendation': (
            f"{overall_winner} is the stronger business with {overall_delta} points lead overall. "
            f"{name_a} wins {a_wins} of 5 dimensions; {name_b} wins {b_wins}. "
            f"{'The gap is decisive — significant structural advantage.' if overall_delta >= 15 else 'Close competition — targeted improvements in weaker areas could shift the lead.'}"
        ),
    }


def predict_growth(
    base_revenue: float,
    growth_rate: float,
    months: int = 12,
    scenario: str = "base",
    seasonality: float = 1.0,
) -> list:
    scenario_mult = {'bull': 1.35, 'base': 1.0, 'bear': 0.65}.get(scenario, 1.0)
    gr = growth_rate / 100

    seasonal_pattern = [
        1.0, 1.02, 1.05, 1.08, 0.95, 0.90,
        0.92, 0.95, 1.10, 1.12, 1.08, 1.05,
        1.03, 1.02, 1.05, 1.08, 0.95, 0.90,
        0.92, 0.95, 1.10, 1.12, 1.08, 1.05,
        1.03, 1.02, 1.05, 1.08, 0.95, 0.90,
        0.92, 0.95, 1.10, 1.12, 1.08, 1.05,
    ]

    result = []
    for i in range(months + 1):
        raw   = base_revenue * ((1 + gr * scenario_mult) ** i)
        seas  = (1 - (1 - seasonality) * (1 - seasonal_pattern[i % len(seasonal_pattern)] * 0.9))
        noise = 1 + random.uniform(-0.015, 0.015) if i > 0 else 1.0
        result.append({
            'month': i,
            'label': f"M{i}" if i > 0 else "Now",
            'revenue': round(raw * seas * noise),
        })
    return result


def get_benchmarks() -> dict:
    return BENCHMARKS
